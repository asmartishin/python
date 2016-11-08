import requests
from requests.packages.urllib3.util.retry import Retry
from requests.adapters import HTTPAdapter
import json
from lib import utils
from lib.logger import Logger
from pymongo import MongoClient
from pprint import pprint
from multiprocess import Pool
import multiprocess
import itertools


logger = Logger().log


class nullCollection():
    pass


class duplicateId():
    pass


class ApiConnector(object):
    def __init__(self, config):
        self.api = config['api']
        self.session = requests.Session()
        self.session.mount(
            self.api, HTTPAdapter(
                max_retries=Retry(
                    total=10, backoff_factor=0.1)))
        self.session.headers.update({
            'Content-Type': 'application/json',
            'Authorization': 'Oauth ' + config['token']
        })
        self.queues = self.get_queues()

    def make_api_request(self, path, data={}):
        try:
            return json.loads(self.session.post(
                self.api + path, data=json.dumps(data)).text)
        except Exception as e:
            logger.error('{}: {}'.format(e.__class__.__name__, e))

    def search_tickets(self, search_conditions):
        for ticket in self.make_api_request(
                '/tickets/find/', search_conditions)['value']:
            yield {
                'ticket_id': ticket['id'],
                'ctime': 'ctime'
            }

    def get_new_tickets(self, from_time=utils.pre_day_to_string(1)):
        search_conditions = {
            "skip": 0,
            "query": {
                "ctimeGte": "{}T21:00:00.000Z".format(from_time),        
                "creationTimeLte": "{}T21:00:00.000Z".format(to_time)
             },
        }
        pool_size = multiprocess.cpu_count()
        pool_volume = 10 * pool_size
        index = 0
        tickets_num = self._get_number_of_tickets(from_time, to_time)
        req_num = utils.ceil_division(tickets_num, 1000)
        pool = Pool(pool_size)
        for req_count in range(req_num):
            search_tickets = self.search_tickets(search_conditions)
            while True:
                tickets = pool.map(self.add_attr_to_ticket, itertools.islice(search_tickets, pool_volume))
                if tickets:
                    print('Downloaded {}/{} tickets'.format(index, tickets_num), end='\r')
                    index += pool_volume
                    yield tickets
                else:
                    break
            search_conditions['skip'] += 1000

    def _get_number_of_tickets(self, from_time):
        search_conditions = {"skip": 0, "query": {"ctimeLte": "{}T21:00:00.000Z".format(from_time)}}
        return self.make_api_request('/tickets/find/', search_conditions)['total']
