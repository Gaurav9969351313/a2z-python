from nsetools import Nse
nse = Nse()
print nse
q = nse.get_quote('infy')
from pprint import pprint
pprint(q)
