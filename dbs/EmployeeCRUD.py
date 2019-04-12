import mysql.connector
#import DBCaller.getConnected
def getConnected():
    con=mysql.connector.connect(
        host='localhost',database='mydb',
        user='root', password='root')
    return con

con=getConnected()
class EmployeeCRUD:
   def  addEmployee(self,fname,lname,age,gen,income):
        sql ="insert into employee(first_name,last_name,age,gender,income) values('"+fname+"','"+lname+"',"+str(age)+",'"+gen+"',"+str(income)+")"
        cur=con.cursor()
        cur.execute(sql)
        print("Added Record")
   def  delEmpl(self,id):
        sql ="delete from Employee where emp_id=%d"%id
        cur=con.cursor()
        cur.execute(sql)

   def  updEmpl(self,id,sal):
        sql ="Update Employee set income=income+"+sal+" where emp_id=%d"%id
        cur=con.cursor()
        cur.execute(sql)

   def  qryEmp(self):
        sql ="select * from employee"
        cur=con.cursor()
        cur.execute(sql)
        results = cursor.fetchall()
        for col in results:
            fname  = col[1]
            lname  = col[2]
            age    = col[3]
            gender = col[4]
            income = col[5]
            # Now print fetched result
            print(fname, lname, age, gender, income )

emp=EmployeeCRUD()
emp.addEmployee('Sanjana','Rai',21,'F',35000)