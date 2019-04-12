import MySQLdb
# Open database connection
con = MySQLdb.Connect(host="127.0.0.1", port=3306, user="root", 
passwd="root", db="mydb")

# prepare a cursor object using cursor() method
cursor = con.cursor()
# Prepare SQL query to UPDATE required records
sql = """DELETE FROM EMPLOYEE WHERE AGE > '%d'"""/
%( int(input('enter Age to Delete')))
try:
    # Execute the SQL command
    cursor.execute(sql)
    # Commit your changes in the database
    con.commit()    
    print ("Record deleted")
except:
    # Rollback in case there is any error
    con.rollback()
# disconnect from server
con.close()