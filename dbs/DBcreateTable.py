#import MySQLdb
import mysql.connector
# Open database connection
#con =  MySQLdb.Connect(host="127.0.0.1", port=3306, user="root", passwd="root", db="mydb")
# prepare a cursor object using cursor() method
con=mysql.connector.connect(host='localhost',database='mydb', user='root', password='root')
cursor = con.cursor()
sql = "CREATE table EMPL(FIRST_NAME varchar(20),LAST_NAME varchar(20), AGE int, Gender char(1), INCOME double) "
try:
   # Execute the SQL command
   cursor.execute(sql)
   print("Table created")
   print(sql)
   # Commit your changes in the database
   con.commit()
except  Exception as e:
   # Rollback in case there is any error
   con.rollback()
   print(e)
# disconnect from server 
con.close() 