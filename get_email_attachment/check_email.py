#!/usr/bin/env python3

import sys
import imaplib
import email
import argparse
import re
import pymorphy2


def parse_arguments():
    parser = argparse.ArgumentParser(description='Script for parsing emails')
    parser.add_argument('-u', '--user', type=str, required=True, help='User login')
    parser.add_argument('-p', '--password', type=str, required=True, help='User password')
    parser.add_argument(
        '-f', '--folder', type=str, required=False, default='search-abuse', help = 'Folder with emails'
    )
    return vars(parser.parse_args())


class MailBox(object):
    EMAL_SERVER_HOSTNAME = 'imap.mail.ru'
    EMAL_SERVER_PORT = 993
    EMAIL_ATTACHMENT_EXTENSION = 'rtf'

    def __init__(self, user, password, folder):
        self._connection = self._connect(user, password, folder)
        self._morph = pymorphy2.MorphAnalyzer()

    @classmethod
    def _connect(cls, user, password, folder):
        assert isinstance(cls.EMAL_SERVER_PORT, int)

        connection = imaplib.IMAP4_SSL(cls.EMAL_SERVER_HOSTNAME, cls.EMAL_SERVER_PORT)

        try:
            connection.login(user, password)
            connection.select(folder)
        except imaplib.IMAP4.error as exception:
            print(exception)
            sys.exit(1)

        return connection

    def check_emails(self):
        result, messages_ids = self._connection.search(None, 'ALL')

        for message_id in messages_ids[0].decode('utf-8').split(' '):
            result, message_data = self._connection.fetch(message_id,'(RFC822)')

            message = email.message_from_bytes(message_data[0][1])

            for message_part in message.walk():
                if message_part.get_content_maintype() != 'multipart' and \
                        message_part.get('Content-Disposition') is not None:
                    filename = message_part.get_filename()
                    if filename and filename.endswith(self.EMAIL_ATTACHMENT_EXTENSION):
                        rtf_text = strip_rtf(message_part.get_payload(decode=True)).encode('latin1').decode('cp1251')
                        print(rtf_text)

    def _disconnect(self):
        self._connection.logout()

    def __del__(self):
        self._disconnect()


def main(*args, **options):
    user = options.get('user')
    password = options.get('password')
    folder = options.get('folder')

    mailbox = MailBox(user, password, folder)
    mailbox.check_emails()


if __name__ == '__main__':
    main(**parse_arguments())
