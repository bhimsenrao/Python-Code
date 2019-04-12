import mysql.connector
# Open database connection
con = mysql.connector.connect(host='localhost',
                    database='mydb',user='root',
                    password='root')
# prepare a cursor object using cursor() method
cursor = con.cursor()
sql = "INSERT INTO EMPLOYEE(FIRST_NAME,LAST_NAME, AGE, GENDER, INCOME) \
       VALUES ('%s', '%s', '%d', '%c', '%d' )" % \
      (input('first name '), input('last name '),int(input('age ')), input('Gender M or F '), int(input('Salary ')))
#sql = """INSERT INTO EMPLOYEE(FIRST_NAME,
#         LAST_NAME, AGE, GENDER, INCOME)
#         VALUES ('"""+input('enter firstname')+"""', 'Kumar', 2, 
#         'M', 4300)"""
try:   # Execute the SQL command
   cursor.execute(sql)
   print (sql)
   con.commit()   # Commit your changes in the database
except Exception as e:
   con.rollback() # Rollback in case there is any error
   print (e)
con.close() # disconnect from server