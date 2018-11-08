import sqlite3 as lite
import sys


con = lite.connect('test.db')

with con:    
    
    cur = con.cursor()
    cur.execute('SELECT SQLITE_VERSION()')
    data = cur.fetchone()
    print "SQLite version: %s" % data # Version print               
    
    cur.execute("SELECT * FROM Cars") #fetch all rows
    rows = cur.fetchall()
    for row in rows:
        print row 
    cur.execute("drop table Friends")
   

    cur.executescript("""  CREATE TABLE if not exists Friends(Id INTEGER PRIMARY KEY, Name TEXT);
                           INSERT INTO Friends(Name) VALUES ('Tom');
                          INSERT INTO Friends(Name) VALUES ('Rebecca');
                           INSERT INTO Friends(Name) VALUES ('Jim');
                          INSERT INTO Friends(Name) VALUES ('Robert');
                   """)

    lid = cur.lastrowid
    print lid

    print ""
    cur.execute("SELECT * FROM Friends")
    rows = cur.fetchall()
    for row in rows:
        print row
    print ""

    print ""                                  # retrieve one by one cur.rowcount after affet of DML
    cur.execute("SELECT * FROM Cars")

    while True:
        row = cur.fetchone()
        if row == None:
            break
        print  row[1], row[2]
    print ""
    
#parameterised query
    uId = 4
    cur.execute("SELECT Name, Price FROM Cars WHERE Id=:Id", 
        {"Id": uId})        
    con.commit()
    
    row = cur.fetchone()
    print ""
    print row[0], row[1]

    print ""
    cur.execute('PRAGMA table_info(Cars)')
    data = cur.fetchall()
    for d in data:
        print d[0], d[1], d[2]
    print ""

#heading printing
    cur.execute('SELECT * FROM Cars')
    col_names = [cn[0] for cn in cur.description]
    rows = cur.fetchall()
    print (col_names[0], col_names[1], col_names[2])
    print ""

#all tables
    print ""
    cur.execute("SELECT name FROM sqlite_master WHERE type='table'")
    rows = cur.fetchall()
    for row in rows:
        print row[0]
    print ""    
con.commit()
    
if con:
        con.close() 
