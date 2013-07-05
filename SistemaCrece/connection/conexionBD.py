'''
Created on 03/07/2013

@author: The Forsaken
'''
import MySQLdb

# connect
db = MySQLdb.connect(host="localhost", user="root", passwd="admin", db="bdcrece" )

cursor = db.cursor()

# execute SQL select statement
cursor.execute("SELECT * FROM area")

# get the number of rows in the resultset
numrows = int(cursor.rowcount)

# get and display one row at a time.
for x in range(0,numrows):
    row = cursor.fetchone()
    print row[0], "-->", row[1]