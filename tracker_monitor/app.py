#!/usr/bin/env python3

import requests
from pprint import pprint
import json
import config
import argparse
import logging
from threading import Thread
import time
from datetime import datetime
import dateutil.parser
from datetime import datetime, timedelta
import os
import smtplib
import socket
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


class CommentNotifier(object):
    def __init__(self, args):
        self.queue = args.queue
        self.comment = args.comment
        self.email = args.email
        self.data_file = args.data_file
        self.start_time = args.start_time
        self.debug_file = config.debug_file
        self.token = config.token
        self.log = None
        self.cache = []
        self.cache_updater = None
        self.cache_update_interval = args.update_interval

        self._config_logger()
        self._populate_cache()
        self._spawn_cache_updater()

    def _config_logger(self):
        self.log = logging.getLogger('app')
        handler = logging.FileHandler(self.debug_file)
        console = logging.StreamHandler()
        handler.setFormatter(logging.Formatter(
            '[%(asctime)s] [%(levelname)s] %(message)s',
            datefmt='%d/%m/%Y %H:%M:%S')
        )
        self.log.addHandler(handler)
        self.log.addHandler(console)
        self.log.setLevel(logging.DEBUG)

    def _populate_cache(self):
        if os.path.isfile(self.data_file) and os.stat(self.data_file).st_size > 0:
            data = self.read_file(self.data_file, 'json')
            if data['queue'] == self.queue and data['comment'] == self.comment and data['start_time'] == self.start_time:
                self.cache = data['data']
                self.log.info('Cache loaded from file')
            else:
                self.cache = self.get_comment_data()
                self.log.info('Cache loaded from tracker')
                data = {'queue': self.queue, 'comment': self.comment, 'start_time': self.start_time, 'data': self.cache}
                self.write_to_file(self.data_file, data, 'json')
        else:
            self.cache = self.get_comment_data()
            self.log.info('Cache loaded from tracker')
            data = {'queue': self.queue, 'comment': self.comment, 'start_time': self.start_time, 'data': self.cache}
            self.write_to_file(self.data_file, data, 'json')

    def _spawn_cache_updater(self):
        self.log.info('Spawning updater ({}s)'.format(self.cache_update_interval))
        self.cache_updater = Thread(
            target=self._update_cache,
            daemon=True
        )
        self.cache_updater.start()

    def _update_cache(self):
        while True:
            cache = self.get_comment_data()
            email_tickets = []
            email_count = 0
            self.log.info('Commments processing')
            for ticket_id, value in cache.items():
                if ticket_id in self.cache:
                    if self.cache[ticket_id]['match_count'] < value['match_count']:
                        email_tickets.append(ticket_id)
                        email_count += value['match_count'] - self.cache[ticket_id]['match_count']
                else:
                    email_tickets.append(ticket_id)
                    email_count += value['match_count']
            if email_count > 0:
                send_email(self.queue, self.comment, self.email, email_tickets, email_count)
                self.log.info('Email send. Queue: {}, comment: {}, email: {}, tickets {}, count: {}'
                              .format(self.queue, self.comment, self.email, email_tickets, email_count))
            self.cache = cache
            self.log.info('Cache updated')
            data = {'queue': self.queue, 'comment': self.comment, 'start_time': self.start_time, 'data': self.cache}
            self.write_to_file(self.data_file, data, 'json')
            time.sleep(self.cache_update_interval)

    def get_comment_data(self):
        try:
            self.log.info('Comments downloading')
            request = {'filter': {'queue': self.queue, 'updated': {'from': self.start_time}}}
            result = {}
            cache = {}

            tickets_num = json.loads(requests.post(
                'https://tracker.ru/issues/_count',
                data=json.dumps(request),
                headers={
                    'Content-Type': 'application/json',
                    'Authorization': 'OAuth ' + self.token}).text)
            tickets = json.loads(requests.post(
                'https://tracker.ru/issues/_search?perPage={}&expand=comments'.format(tickets_num),
                data=json.dumps(request),
                headers={
                    'Content-Type': 'application/json',
                    'Authorization': 'OAuth ' + self.token}).text)
            for ticket in tickets:
                if 'comments' in ticket:
                    cache[ticket['key']] = {'comments_ctime': [], 'match_count': 0}
            for ticket_id, value in cache.items():
                comments = json.loads(
                    requests.get(
                        'https://tracker.ru/issues/{}/comments'.format(ticket_id),
                        headers={
                            'Content-Type': 'application/json',
                            'Authorization': 'OAuth ' + self.token})
                        .text)
                for comment in comments:
                    if self.comment in comment['text']:
                        value['comments_ctime'].append((dateutil.parser.parse(comment['updatedAt']) + \
                                                        timedelta(hours=3)).strftime("%Y-%m-%d %H:%M:%S"))
                        value['match_count'] += 1
                if value['match_count'] > 0:
                    result[ticket_id] = value
            return result
        except Exception as e:
            self.log.error('Comments download failed {}: {}'.format(e.__class__.__name__, e))

    read_file = lambda self, filename, filetype=None: json.load(open(filename)) \
        if filetype and filetype.lower() == 'json' else open(filename).readlines()

    write_to_file = lambda self, filename, data, filetype=None: json.dump(data, open(filename, 'w+')) \
        if filetype and filetype.lower() == 'json' else open(filename, 'w+').writelines(data)


def send_email(queue, comment, email, tickets, count):
    from_email = socket.gethostname()
    user_email = email

    msg = MIMEMultipart('alternative')
    msg['Subject'] = 'New comment in {} queue'.format(queue)
    msg['From'] = from_email
    msg['To'] = user_email

    html = '''
        <!DOCTYPE html>
        <html>
        <head>
            <title>New comment{s} in {queue}</title>
            <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
        </head>
        <body style="margin: 0; padding: 0;">
        <table border="1" align="center"  cellpadding="0" cellspacing="0" width="300px" style="border-collapse: collapse;">
            <tr>
                <td bgcolor="ffffff">
                    <table  cellpadding="0" cellspacing="0" width="100%" style="padding: 30px 20px 30px 20px">
                        <tr>
                            <td >
                                <table  cellpadding="0" cellspacing="0" width="100%">
                                    <tr>
                                        <td>
                                            <center>
                                                <b>{count}</b> new '<b>{comment}</b>' comment{s}<br>
                                                in <span style='word-wrap: normal'><b>{tickets}</b></span> ticket{s} <br>
                                                in <b>{queue}</b> queue
                                            </center>
                                        </td>
                                    </tr>
                                </table>
                            </td>
                        </tr>
                    </table>
                </td>
            </tr>
        </table>
        </body>
        </html>
        '''.format(queue=queue, s='s' if count > 1 else '', tickets=tickets, count=count, comment=comment)
    msg.attach(MIMEText(html, 'html'))
    s = smtplib.SMTP('localhost')
    s.sendmail(from_email, user_email, msg.as_string())
    s.quit()


def parse_arguments():
    parser = argparse.ArgumentParser(description='Script for email notification for new commnets in tickets')
    parser.add_argument('-q', '--queue', type=str, required=True,
                        help='Queue to parse comments from')
    parser.add_argument('-c', '--comment', type=str, required=True,
                        help='Comment to parse from queue')
    parser.add_argument('-e', '--email', type=str, required=True,
                        help='Email to send notifications to')
    parser.add_argument('-f', '--data_file', type=str, required=False, default='data.json',
                        help='Output file')
    parser.add_argument('-t', '--start_time', type=str, required=False, default=datetime.now().strftime("%Y-%m-%d"),
                        help='Start time')
    parser.add_argument('-r', '--update_interval', type=int, required=False, default=config.update_interval,
                        help='Update interval')
    return parser.parse_args()


def main():
    args = parse_arguments()
    comment_notifier = CommentNotifier(args)


if __name__ == '__main__':
    main()
    input()
