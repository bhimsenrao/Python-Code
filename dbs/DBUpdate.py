import MySQLdb

# Open database connection
con = MySQLdb.Connect(host="127.0.0.1", port=3306, user="root", 
passwd="root", db="mydb")
# prepare a cursor object using cursor() method
cursor = con.cursor()
# Prepare SQL query to UPDATE required records
sql = "UPDATE EMPLOYEE SET AGE = 18 WHERE First_Name= '%s'"
 % input('name of person')
try:
    # Execute the SQL command
    cursor.execute(sql)
    # Commit your changes in the database
    con.commit()
    print ("Updated record")
except:
    # Rollback in case there is any error
    con.rollback()
# disconnect from server
con.close()