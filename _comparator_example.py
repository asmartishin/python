#!/usr/bin/env python

import re
import urlparse
from urllib import urlencode
import re

regexp_ace = re.compile(r'xn--')
regexp_schemes_http = re.compile(r'^https?://')
regexp_www = re.compile(r'^www\.')
regexp_schemes = re.compile('^([a-z][a-z0-9+\-.]*):')
regexp_domain_element = re.compile('^([a-z0-9]{1}[-a-z0-9]*[a-z0-9]{1}|[a-z0-9])$')


class BaseError(Exception):
    pass


class AnalyseUrlException(BaseError):
    pass


class BadUrlException(AnalyseUrlException):
    pass


class BadLevelException(BadUrlException):
    pass


class AnalyseUrl(object):
    ELEMENT_MAX_LENGTH = 63
    MIN_DOMAIN_LEVEL = 2
    MAX_URL_LENGTH = 2048

    def __init__(self, url, strict=True):
        self.__url = url
        self.__parsed_url = self._parse_url(url, strict)

    def _parse_url(self, url, strict):
        if len(url) > self.MAX_URL_LENGTH:
            raise BadUrlException("Url is too long")

        if regexp_schemes.match(url):
            pass
        elif not regexp_schemes_http.match(url):
            url = 'http://' + url

        try:
            parsed_url = urlparse.urlparse(url)
        except ValueError as e:
            raise BadUrlException("Bad url. Failed to parse it: {}".format(e))

        if not parsed_url.hostname or not parsed_url.scheme:
            raise BadUrlException("Can't get host name from url " + url)

        domain = re.sub(regexp_www, '', parsed_url.hostname)
        domain_elements = domain.split('.')

        if not parsed_url.path and parsed_url.query:
            raise BadUrlException("Url with query but without path " + url)

        has_non_ascii = False
        try:
            parsed_url.hostname.decode('utf8')
        except UnicodeEncodeError:
            has_non_ascii = True

        if regexp_ace.search(parsed_url.hostname) or has_non_ascii is False:
            pass
        else:
            try:
                parsed_url = parsed_url._replace(netloc=parsed_url.hostname.encode('idna'))
            except UnicodeError:
                raise BadUrlException("Something wrong with url {} to be analyzed".format(url))

        if strict:
            level = len(domain_elements)
            if level < AnalyseUrl.MIN_DOMAIN_LEVEL:
                raise BadLevelException("Strict check.")

            for element in domain_elements:
                if not element or not regexp_domain_element.match(element.encode('idna')) or \
                                len(element) > AnalyseUrl.ELEMENT_MAX_LENGTH:
                    raise BadUrlException("Strict check. Invalid url " + url)

        return parsed_url

    def get_parsed_url_obj(self):
        return self.__parsed_url

    def get_url(self, human_readable=False):
        if human_readable and regexp_ace.search(self.__parsed_url.hostname):
            return self.__parsed_url._replace(netloc=self.__parsed_url.hostname.decode('idna')).geturl()
        return self.__parsed_url.geturl()

    def get_canonical_url(self):
        """
        Strip scheme, www and / at the end
        """
        parsed_obj = self.get_parsed_url_obj()
        query = "?" + parsed_obj.query if parsed_obj.query else ""
        return self.get_hostname_without_www() + parsed_obj.path.rstrip('/') + "/" + query

    def get_hostname(self, human_readable=False):
        if human_readable and regexp_ace.search(self.__parsed_url.hostname):
            return self.__parsed_url.hostname.decode('idna')
        return self.__parsed_url.hostname

    def get_hostname_without_www(self, human_readable=False):
        hostname = self.get_hostname(human_readable)
        return re.sub(regexp_www, '', hostname)

    def get_scheme(self):
        return self.__parsed_url.scheme

    def has_www(self):
        return True if regexp_www.search(self.__parsed_url.hostname) else False

    def is_https(self):
        return self.get_scheme() == 'https'

    def add_query_param(self, params):
        assert isinstance(params, dict)
        query = {x[0].encode('utf-8'): x[1].encode('utf-8') for x in urlparse.parse_qsl(self.__parsed_url.query)}
        query.update(params)
        # Hack! Bad code! urlparse object has no setters
        self.__parsed_url = self.__parsed_url._replace(query=urlencode(query))
        return self


class Url(object):
    def __init__(self, url):
        self.url = url
        self.canonical_url = AnalyseUrl(url=self.url, strict=False).get_canonical_url()

    def __eq__(self, other):
        return self.canonical_url == self.canonical_url

    def __repr__(self):
        return self.url

    def __hash__(self):
        return hash(self.canonical_url)


if __name__ == '__main__':
    urls1 = set(Url(x) for x in ['https://www.drive2.ru/market/offers/186435', 'https://www.drive2.ru/market/offers/36458', 'http://www.drive2.ru/market/offers/219264', 'https://www.drive2.ru/market/offers/229461', 'https://www.drive2.ru/market/offers/229459', 'https://www.drive2.ru/market/offers/219263', 'https://www.drive2.ru/market/offers/165712', 'https://www.drive2.ru/market/offers/207739', 'https://www.drive2.ru/market/offers/207742', 'https://www.drive2.ru/market/offers/219262'])
    urls2 = set(Url(x) for x in ['https://www.drive2.ru/market/offers/219266', 'https://www.drive2.ru/market/offers/199119', 'https://www.drive2.ru/market/offers/219265', 'https://www.drive2.ru/market/offers/186435', 'https://www.drive2.ru/market/offers/36458', 'https://www.drive2.ru/market/offers/219264', 'https://www.drive2.ru/market/offers/229461', 'https://www.drive2.ru/market/offers/229459', 'https://www.drive2.ru/market/offers/219263', 'https://www.drive2.ru/market/offers/165712'])
    print(urls1.difference(urls2))
