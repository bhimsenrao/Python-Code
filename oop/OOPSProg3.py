class Person:
    id=0
    pname=None
    
    #constructor for current class
    def __init__(self):
        print("Object ready to use")
    # destructor of the class
    def __del__(self):
        print("Object released from runtime")
   #mutation and Accessibility of properties
    def getId(self): 
       return self.id
    def getPname(self):
        return self.pname   
    
    def setId(self,id):
        self.id=id
    def setPname(self,name):
        self.pname=name;
# create the object of the class
p=Person()
p.setId(101)
p.setPname("Raju")
print(p.id,'  ',p.getPname())
