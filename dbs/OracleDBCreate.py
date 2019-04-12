#import MySQLdb
# Open database connection
import mysql.connector
con =  mysql.connector.connect(host='localhost',
                    database='mydb',user='root',
                    password='root')
#MySQLdb.Connect(host="127.0.0.1", port=3306, user="root", passwd="root", db="mydb")
# prepare a cursor object using cursor() method
cursor = con.cursor()
sql = """CREATE table EMPLOYEE(FIRST_NAME varchar(20),
         LAST_NAME varchar(20), AGE int, Gender char(1), INCOME double) """
try:
   # Execute the SQL command
   cursor.execute(sql)
   # Commit your changes in the database
   db.commit()
except:
   # Rollback in case there is any error
   db.rollback()
# disconnect from server
con.close()