
from nsetools import Nse
from pprint import pprint
import sqlite3 as lite
import sys


con = lite.connect('test.db')
nse = Nse()

stockstoPull = '20MICRONS','3IINFOTECH','3MINDIA','8KMILES','A2ZINFRA','AARTIDRUGS'


for stkVal in stockstoPull:     # First Example
   print 'Current Stock :', stkVal
   q = nse.get_quote(stkVal)
   varmar = q['varMargin']
   varsym = q['symbol']
   varh52 = q['high52']
   varl52 = q['low52']
   vardh = q['dayHigh']
   vardl = q['dayLow']
   varlstp = q['lastPrice']
   varapm = q['applicableMargin']
   varclp = q['closePrice']
   varavp = q['averagePrice']
   print "varMargin is" ,varsym
   print varh52
   print varl52
   print vardh
   print vardl
   print varlstp
   print varapm
   #print varclp
   print varmar
   print varavp

   stkdata = (varh52, varl52, vardh, vardl, varlstp, varapm, varmar,varavp)
   with con:    
    cur = con.cursor()
    cur.execute("drop table StockMaster")
    cur.execute("CREATE TABLE if not exists StockMaster(varMargin varchar(10),symbol varchar(10),high52 varchar(10),dayHigh varchar(10),dayLow varchar(10),lastPrice varchar(10),closePrice varchar(10),averagePrice varchar(10))")
    cur.executemany("INSERT INTO StockMaster values(?,?,?,?,?,?,?,?)", stkdata)
    con.commit()
    
    rows = cur.fetchall()
    for row in rows:
        print row
    if con:
        con.close()


