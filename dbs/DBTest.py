#import MySQLdb
import mysql.connector
# Open database connection
#con =  MySQLdb.Connect(host="127.0.0.1", 
#port=3306, user="root", passwd="root", db="mydb")
# prepare a cursor object using cursor() method
con=mysql.connector.connect(host='localhost',
                    database='mydb',user='root',   password='root')
cursor = con.cursor()
cursor.execute("SELECT VERSION()") 
# execute SQL query using execute() method.
data = cursor.fetchone() # Fetch a single row using fetchone() method.
print ("Database version : %s " % data)
con.close()  # disconnect from server 