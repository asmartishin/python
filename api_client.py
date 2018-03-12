# -*- coding: utf-8 -*-

from collections import namedtuple
import requests
from requests.packages.urllib3.util.retry import Retry
from requests.adapters import HTTPAdapter
import logging
from sys import stdout
from functools import wraps
import urllib
from urlparse import urljoin

API_CLIENT_TIMEOUT = 60
API_RETRIES_COUNT = 3
API_BACKOFF_FACTOR = 0.1
API_BAD_STATUSES = (500, 502, 503, 504)

log = logging.getLogger(__name__)
logging.basicConfig(stream=stdout, format="%(asctime)s %(levelname)s %(message)s")


class ApiClientError(Exception):
    def __init__(self, *args):
        self.logged = False
        super(ApiClientError, self).__init__(*args)


class ApiClientHttpError(ApiClientError):
    pass


def path(relative_url):
    def function_decorator(func):
        @wraps(func)
        def function_wrapper(self, *args, **kwargs):
            api_path = urljoin(self._base_url, relative_url)
            return func(self, api_path, *args, **kwargs)
        return function_wrapper
    return function_decorator


def log_exceptions(logger):
    def function_decorator(func):
        @wraps(func)
        def function_wrapper(self, *args, **kwargs):
            try:
                return func(self, *args, **kwargs)
            except Exception as e:
                if hasattr(e, 'logged') and not e.logged:
                    e.logged = True
                    logger.error(e.message)
                raise
        return function_wrapper
    return function_decorator


class LogExceptionsMetaClass(type):
    def __new__(mcs, name, bases, cls_dict):
        new_cls_dict = {}
        for name, attribute in cls_dict.items():
            if callable(attribute):
                attribute = log_exceptions(log)(attribute)
            new_cls_dict[name] = attribute
        return type.__new__(mcs, name, bases, new_cls_dict)


ApiErrors = namedtuple("ApiErrors", "basic http")


class ApiClient(object):
    __metaclass__ = LogExceptionsMetaClass

    API_ERRORS = ApiErrors(ApiClientError, ApiClientHttpError)

    def __init__(self, base_url, oauth_token=None):
        if not base_url.endswith('/'):
            base_url += '/'

        self._base_url = base_url
        self._session = requests.Session()

        retries = Retry(
            total=API_RETRIES_COUNT,
            backoff_factor=API_BACKOFF_FACTOR,
            status_forcelist=API_BAD_STATUSES
        )
        self._session.mount(self._base_url, HTTPAdapter(max_retries=retries))

        headers = {
            'Content-Type': 'application/json',
        }

        if oauth_token:
            headers['Authorization'] = 'OAuth {}'.format(oauth_token)
        self._session.headers.update(headers)

    def _get(self, url, error_message='GET request failed'):
        try:
            response = self._session.get(url, timeout=API_CLIENT_TIMEOUT)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            raise self._handle_http_error(e, error_message)
        except Exception as e:
            raise self._handle_error(e, error_message)

    def _post(self, url, data=None, json=None, error_message='POST request failed'):
        try:
            response = self._session.post(url, data=data, json=json, timeout=API_CLIENT_TIMEOUT)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            raise self._handle_http_error(e, error_message)
        except Exception as e:
            raise self._handle_error(e, error_message)

    def _put(self, url, data=None, json=None, error_message='PUT request failed'):
        try:
            response = self._session.put(url, data=data, json=json, timeout=API_CLIENT_TIMEOUT)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            raise self._handle_http_error(e, error_message)
        except Exception as e:
            raise self._handle_error(e, error_message)

    @classmethod
    def _handle_http_error(cls, e, error_message):
        error_message = '{} with http error: "{}"'.format(error_message, e.message)
        return cls.API_ERRORS.http(error_message)

    @classmethod
    def _handle_error(cls, e, error_message):
        error_message = '{} with error: "{}"'.format(error_message, e.message)
        return cls.API_ERRORS.basic(error_message)

    @classmethod
    def _build_query(cls, data):
        return urllib.urlencode(data)
