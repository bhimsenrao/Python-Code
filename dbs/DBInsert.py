import mysql.connector
# Open database connection
con =  mysql.connector.Connect(host='localhost',
                    database='mydb',user='root',   password='root')

cursor = con.cursor()
sql = "INSERT INTO Empl(First_name,Last_name,age,gender,income) VALUES ('%s', '%s','%d','%s','%d')#" % ('Vijay','Kumar',21,'m',34000)
try:   # Execute the SQL command
   cursor.execute(sql)
   print (sql)
   con.commit()   # Commit your changes in the database
except Exception as e:
   con.rollback() # Rollback in case there is any error
   print (e)
con.close() # disconnect from server