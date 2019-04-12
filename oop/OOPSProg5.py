class  Employee:
    empid=0
    empname=None
    def storeEmpData(self,id,name):
        self.empid=id
        self.empname=name
    def viewData(self):
        print('Empid=',self.empid,'  empname=',self.empname)

class Department(Employee):    # deparment inherits Employee class
    job=None
    
    def storeDeptData(self,job):
        self.job=job
    def viewData(self):
        super().viewData()   # super() refers parenet class property
        print("Working as ",self.job)

class Location(Department):
    loc=None
    def storeLocation(self,loc1):
        self.loc=loc1
    def viewData(self):
        super().viewData()
        print("I am from %s"%(self.loc))

myLoc=Location()
myLoc.storeEmpData(101,"Manoj")
myLoc.storeDeptData("Sales Manager")
myLoc.storeLocation("Hyderbad")
myLoc.viewData()