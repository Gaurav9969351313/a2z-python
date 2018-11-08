##import pyodbc
##
##
###con = pyodbc.connect('DRIVER={SQL Server};SERVER=172.31.25.48\MSSQLSERVER;DATABASE=SentiMenti;UID=odin;PWD=odin')
##
##con = pyodbc.connect('Trusted_Connection=yes', driver = '{SQL Server}',server = '172.31.25.48\MSSQLSERVER', database = 'SentiMenti')
##                     
##querystring = "select * from SentiMenti"
##cur = con.cursor()
##cur.execute(querystring)
##con.commit()
###print(querystring)


import pypyodbc
import sys
connection = pypyodbc.connect('Driver={SQL Server};'
                              'Server=172.31.7.7;'
                                'Database=FT_IFTTT;'
                                'uid=odin;pwd=odin')
cursor = connection.cursor()


SQLCommand = ("SELECT * from tbl_ScripMaster")
cursor.execute(SQLCommand)
results = cursor.fetchall()

print(results[0][0])
print(len(results))

##i = 0
##while i < len(results):
##  q = results[i][0]
##  print(q)
##  i += 1

totalTokens = len(results)
ix = 0
while ix < totalTokens:
    
    query = results[ix][2]
    print (query)
    number = '1'
    ix += 1

##  
##while results:
##    print ("Your customer " +  results[0])
##    results = cursor.fetchone()
##    connection.close()

SQLCommand = ("insert into token(tokenName, tokenCode,tokenDetails) VALUES(?,?,?)")
Values = ['acc','bc','cd']
cursor.execute(SQLCommand, Values)
connection.commit() 
connection.close()
