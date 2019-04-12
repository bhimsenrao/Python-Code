class  Employee:
    empid=0
    empname=None
    def storeEmpData(self,id,name):
        self.empid=id
        self.empname=name
    def viewData(self):
        print('Empid=',self.empid,'  empname=',self.empname)

class FullTimeEmp(Employee):
    salary=0
    def storeFEmp(self,salary):
        self.salary=salary
    def viewData(self):
        super().viewData()
        print("My Salary is ",self.salary)

class PartTimeEmp(Employee):
    payPerday=0
    totalDays=0
    def storePEmp(self,perDay,tDays):
        amount=perDay*tDays
        super().viewData()
        print("Total Amount Paid ",amount)
#-------------------------------------------#        
print("Full time Emp details")
ft = FullTimeEmp()
ft.storeEmpData(101,"Hari")
ft.storeFEmp(45000)
ft.viewData()
#------------------------------------------#
print("----------Parttime Employee----------------")
pt= PartTimeEmp()
pt.storeEmpData(400,"Jagadish")
pt.storePEmp(2000,20)