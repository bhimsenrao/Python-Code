class Employee:
    empid=0
    def showMessage(self,id):
        print "Hello!",id
        
    def setEmpId(self,id):
        Employee.empid=id
        
    def getEmpid(self):
        return Employee.empid
        

emp= Employee()
emp.showMessage(101)
emp.setEmpId(121)
print emp.getEmpid()

