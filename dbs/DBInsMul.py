#import MySQLdb
# Open database connection
#con =  MySQLdb.Connect(host="127.0.0.1", port=3306, user="root", passwd="root", db="mydb")
# prepare a cursor object using cursor() method
import mysql.connector
con=mysql.connector.connect(host='localhost',database='mydb',  user='root', password='root')
cursor = con.cursor()
sql = "INSERT INTO EMPLOYEE(FIRST_NAME, \
       LAST_NAME, AGE, GENDER, INCOME) \
       VALUES (%s, %s, %s, %s,%s )#" 

rows=[ ("Harish", "Raj", "20", "M", "2000"),
       ('Vamsi', 'Kumar', '20', 'M', '2000')]

try:   # Execute the SQL command
   cursor.executemany(sql,rows)
   print (sql)
   con.commit()   # Commit your changes in the database
except Exception as e:
   con.rollback() # Rollback in case there is any error
   print (e)
con.close() # disconnect from server