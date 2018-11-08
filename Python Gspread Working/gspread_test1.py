import subprocess
import re
import sys
import time
import datetime
import gspread

email = 'gauravtalele1102@gmail.com'
password = 'gauravtalele*123'
spreadsheet = '<YOUR SPREADSHEET NAME>'

try:
    gc = gspread.login(email, password)
except:
    print "Unable to log in. Check your email address/password"
    sys.exit()

try:
#worksheet = gc.open(spreadsheet).sheet1
#gc.open('My fancy spreadsheet')
#gc.open_by_key('0BmgG6nO_6dprdS1MN3d3MkdPa142WFRrdnRRUWl1UFE')
# worksheet = gc.open_by_key('<YOUR SPREADSHEET KEY>')
gc.open_by_url('https://docs.google.com/spreadsheet/ccc?key=0Bm...FE&hl')
except:
    print "Unable to open the spreadsheet. Check your filename: %s" % spreadsheet
    sys.exit()


### write some code here to read serial port




try:
    values = [datetime.datetime.now(), tempC, tempF, humidity]
    worksheet.append_row(values)
except:
    print "Unable to append data. Check your connection?"
    sys.exit()
