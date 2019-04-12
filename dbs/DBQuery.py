#import MySQLdb
# Open database connection
#con =  MySQLdb.Connect(host="127.0.0.1", port=3306, user="root", 
#passwd="root", db="mydb")
import mysql.connector
con=mysql.connector.connect(host='localhost',database='mydb',  user='root', password='root')
sql = "SELECT * FROM EMPLOYEE "
cursor=con.cursor()
try:
   # Execute the SQL command
   cursor.execute(sql)
   # Fetch all the rows in a list of lists.
   results = cursor.fetchall()
   for col in results:
      fname  = col[1]
      lname  = col[2]
      age    = col[3]
      gender = col[4]
      income = col[5]
      # Now print fetched result
      print(fname, lname, age, gender, income )
except Exception as e:
   print ("Error: unable to fecth data ",e)
con.close()
