class Employee:
    id=10
    name="Hari"
    location="delhi"
#    def __init__(self):
#        print "Object created" 
    def __init__(self,id,name):
        self.id=id
        self.name=name
        print ("parameterized")
    def setEmpid(self,id):
        self.id=id
    def setEmpName(self,name):
        self.name=name
    def setLocation(self,location):
        self.location=location
    def getEmpid(self):
        return self.id
    def getEmpName(self):
        return self.name
    def getLocation(self):
        return self.location    
    def __del__(self):
        print ("Object Released" )
    def showDetails(self):
        print (self.id)
        print (self.name)
class JobProfile(Employee):
    designation="executive"
    
    def __init__(self):
        print ("Object created ")
         
    def setDesignation(self,designation):
        self.designation=designation
    def getDesignation(self):
        return self.designation
    
    def showDetails(self):
        super().showDetails()
        print ("Employee ID=",self.id)
        print ("Employee Name=",self.name)
        print ("Employee Location=",self.location)
        print ("Designation=",self.designation)
        
job=JobProfile()
job.setDesignation("Manager")
job.setEmpid(101)
job.setEmpName("Manohar")
job.setLocation("Hyderabad")

job.showDetails()