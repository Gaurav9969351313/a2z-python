
from nsetools import Nse
from pprint import pprint

nse = Nse()

symfile = open("symbolslist.txt")
q = nse.get_quote('infy')

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
print varclp
print varmar
print varavp
