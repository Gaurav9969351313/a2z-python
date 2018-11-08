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
connection = pypyodbc.connect('Driver={SQL Server};'
                              'Server=localhost;'
                                'Database=SentiMenti;'
                                'uid=odin;pwd=odin')
cursor = connection.cursor() 
##SQLCommand = ("SELECT * from token")
##cursor.execute(SQLCommand)
##results = cursor.fetchall()
##
##print(results[2][0])
##print(len(results))
##
##i = 0
##while i < len(results):
##  print(results[i][0])
##  i += 1
##while results:
##    print ("Your customer " +  results[0])
##    results = cursor.fetchone()
##    connection.close()

SQLCommand = ("insert into token(tokenName, tokenCode,tokenDetails) VALUES(?,?,?)")
Values = ['ab','bc','cd']
cursor.execute(SQLCommand, Values)
connection.commit() 
connection.close()
