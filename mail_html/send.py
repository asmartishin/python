#!/usr/bin/env python3

import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

author = "noreply@node.mytty.ru"
recipient = "monkey@yandex-team.ru"
#recipient = "alex.martishin@yandex.ru"

msg = MIMEMultipart('alternative')
msg['Subject'] = 'HTML mail'
msg['From'] = author
msg['To'] = recipient

text = "Hi!\nHow are you?"
html = '''
<!DOCTYPE html>
<html>
<head>
    <title>Test Email</title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
</head>
<body style="margin: 0; padding: 0;">
<table border="1" align="center"  cellpadding="0" cellspacing="0" width="600px" style="border-collapse: collapse;">
    <tr>
        <td align="center" bgcolor="#70bbd9" style="padding: 10px 0 10px 0;">
            <img src="http://node.mytty.ru/img/mail.png" alt="Creating Email Magic" width="170" height="140" style="display: block; margin-left: auto; margin-right: auto"/>
        </td>
    </tr>
    <tr>
        <td bgcolor="ffffff">
            <table  cellpadding="0" cellspacing="0" width="100%" style="padding: 30px 10px 30px 10px">
                <tr>
                    <td style="padding: 10px 0 10px 10px">
                        <table  cellpadding="0" cellspacing="0" width="100%">
                            <tr>
                                <td>
                                    <img src="http://node.mytty.ru/img/left.png" alt="phone" width="80%" height="120"
                                         style="display: block;  margin-left: auto; margin-right: auto"/>
                                </td>
                            </tr>
                            <tr>
                                <td style="padding: 25px 0 0 0;">
                                    Lorem ipsum dolor sit amet, consectetur adipiscing elit. In tempus adipiscing felis, sit
                                    amet blandit ipsum volutpat sed. Morbi porttitor, eget accumsan dictum, nisi libero
                                    ultricies ipsum, in posuere mauris neque at erat.
                                </td>
                            </tr>
                        </table>
                    </td>
                    <td style="font-size: 0; line-height: 0;" width="20">
                        &nbsp;
                    </td>
                    <td width="260" valign="top" style="padding: 10px 10px 10px 0px">
                        <table  cellpadding="0" cellspacing="0" width="100%">
                            <tr>
                                <td>
                                    <img src="http://node.mytty.ru/img/right.png" alt="" width="80%" height="120"
                                         style="display: block; margin-left: auto; margin-right: auto"" />
                                </td>
                            </tr>
                            <tr>
                                <td style="padding: 25px 0 0 0;">
                                    Lorem ipsum dolor sit amet, consectetur adipiscing elit. In tempus adipiscing felis,
                                    sit amet blandit ipsum volutpat sed. Morbi porttitor, eget accumsan dictum, nisi
                                    libero ultricies ipsum, in posuere mauris neque at erat.
                                </td>
                            </tr>
                        </table>
                    </td>
                </tr>
            </table>
        </td>
    </tr>
    <tr>
        <td bgcolor="#ee4c50" style="padding: 30px 30px 30px 30px;">
            <table  cellpadding="0" cellspacing="0" width="100%">
                <tr>
                    <td>
                        <span style="float: left">&reg; Someone, somewhere 2013
                    </td>
                </tr>
            </table>
        </td>
    </tr>
</table>
</body>
</html>
'''
part1 = MIMEText(text, 'plain')
part2 = MIMEText(html, 'html')

msg.attach(part1)
msg.attach(part2)

s = smtplib.SMTP('localhost')

s.sendmail(author, recipient, msg.as_string())
s.quit()
