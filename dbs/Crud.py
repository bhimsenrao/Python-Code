import mysql.connector
from DBCaller import getConnected
#con=mysql.connector.connect(host='localhost',database='mydb',
#                            user='root', password='root')
con=getConnected()
class Person:
    def addRecord(self,id,name):
        try:
            cur=con.cursor()
            cur.execute("insert into person values('"+str(id)+"','"+name+"')")
            con.commit()
            print("record added")
        except Exception as e:
            print(e)
    def updateRecord(self):
            #your code here
            return
    def viewAllPersons(self):
            cur=con.cursor()
            cur.execute("select * from person")
            result=cur.fetchall()
            for row in result:
                for col in row:
                    print(col,end="   ")
                print("")
p=Person()
p.viewAllPersons()