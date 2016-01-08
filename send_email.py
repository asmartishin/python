#!/usr/bin/env python

import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEBase import MIMEBase
from email import Encoders

def emailSend(EMAIL_RECIPIENTS):
    SUBJECT = "Test Email with attachment"
    msg = MIMEMultipart()
    msg['Subject'] = SUBJECT
    msg['From'] = 'noreply'
    msg['To'] = ', '.join(EMAIL_RECIPIENTS)
    part = MIMEBase('application', "octet-stream")
    part.set_payload(open("test.txt", "rb").read())
    Encoders.encode_base64(part)
    part.add_header('Content-Disposition', 'attachment; filename="test.txt"')
    msg.attach(part)
    server = smtplib.SMTP('localhost')
    server.sendmail('iam@monkeyd.ru', EMAIL_RECIPIENTS, msg.as_string())

if __name__ == '__main__':
    emailSend('alex.martishin@yandex.ru')
