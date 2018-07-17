# -*- coding: utf-8 -*-

import urllib
from urlparse import urljoin

import requests
from requests.packages.urllib3.util.retry import Retry
from requests.adapters import HTTPAdapter

API_CLIENT_TIMEOUT = 60
API_RETRIES_COUNT = 3
API_BACKOFF_FACTOR = 0.1
API_BAD_STATUSES = (500, 502, 503, 504)


class ApiClientError(Exception):
    pass


class ApiClientHttpError(ApiClientError):
    pass


def handle_error(default_error, custom_errors=None):
    if custom_errors is None:
        custom_errors = {}

    def function_decorator(func):
        @wraps(func)
        def function_wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except Exception as e:
                try:
                    error = custom_errors[type(e)](e)
                except (KeyError, TypeError):
                    error = default_error(e)
                raise error
        return function_wrapper
    return function_decorator


class ApiClient(object):
    handle_error = handle_error(
        default_error=ApiClientError,
        custom_errors={
            requests.RequestException: ApiClientHttpError,
        }
    )

    def __init__(self, base_url, oauth_token=None, timeout=API_CLIENT_TIMEOUT):
        if not base_url.endswith('/'):
            base_url += '/'

        self._base_url = base_url
        self._session = requests.Session()
        self._timeout = timeout

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

    @handle_error
    def _get(self, url, json_format=True):
        response = self._session.get(url, timeout=self._timeout)
        response.raise_for_status()

        if json_format:
            return response.json()

        return response

    @handle_error
    def _post(self, url, data=None, json=None, json_format=True):
        response = self._session.post(url, data=data, json=json, timeout=self._timeout)
        response.raise_for_status()

        if json_format:
            return response.json()

        return response

    @handle_error
    def _put(self, url, data=None, json=None, json_format=True):
        response = self._session.put(url, data=data, json=json, timeout=self._timeout)
        response.raise_for_status()

        if json_format:
            return response.json()

        return response

    @classmethod
    def _build_query(cls, data):
        return urllib.urlencode(data)

    def _build_url(self, relative_url, *args, **kwargs):
        url = urljoin(self._base_url, relative_url)

        if kwargs:
            query = self._build_query(kwargs)
            args = args + (query,)

        return url.format(*args)
