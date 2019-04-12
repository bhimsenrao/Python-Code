class Employee:
    id=10
    name="Hari"
    location="delhi"
    def __init__(self):
        print "Object created" 
    def __init__(self,id,name):
        self.id=id
        self.name=name
        print "parameterized"
    def __del__(self):
        print "Object Released"
        
    def showDetails(self):
        print self.id
        print self.name
    def showDetails(self,location):
        print("{0},{1}".format(self.id,self.name)),location
try:
 emp1= Employee(101,'kiran')
 emp1.showDetails("Hyd")
except Exception as e1:
 print (e1)
finally:
 print ("End of program")
    