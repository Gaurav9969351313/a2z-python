#!/usr/bin/python

import time
import smtplib

from nsetools import Nse
nse = Nse()
q = nse.get_quote('infy')
from pprint import pprint
pprint(q)

str1 = str(q)

#print str1
"""
#Working code
TO = 'gauravtalele1102@gmail.com'
SUBJECT = '||Shree Swami Samartha|| mail sent from python'
TEXT = 'hii gaurav here is Your mail'

gmail_sender = 'gauravtalele@gmail.com'
gmail_passwd = 'gauravtalele*123'

server = smtplib.SMTP('smtp.gmail.com',587)
server.ehlo()
server.starttls()
server.ehlo()
server.login(gmail_sender, gmail_passwd)
BODY = '\n'.join([
        'To: %s' % TO,
        'From: %s' % gmail_sender,
        'Subject:%s' % SUBJECT,
        '',
        str1

        ])

try:
        server.sendmail(gmail_sender,[TO], BODY)
        print 'email sent'
except:
        print 'error sending mail'

time.sleep(5)

server.quit()
"""
