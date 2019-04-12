class Student:
    __id=0
    __name=None
    def setData(self,id,name):
        self.__id=id
        self.__name=name
    def viewData(self):
        print(self.__id,self.__name)
class Score(Student):
    __sub1=0
    __sub2=0
    def getSub1(self):
        return self.__sub1
    def getSub2(self):
        return self.__sub2
    def setData(self,id,name,sub1,sub2):
        super().setData(id,name)
        self.__sub1=sub1
        self.__sub2=sub2
    def viewData(self):
        super().viewData()
        print(s elf.__sub1,self.__sub2) 
class Grade(Score):
    total=0
    avr=0
    def evalGrade(self):
        self.total=self.getSub1()+self.getSub2()
        self.avr=self.total/2.0
        if (self.getSub1()<35 or self.getSub2()<35 ):
            print("Failed")
        else:    
            if( self.avr>=60):
                print("First")
            elif(self.avr>=50 and self.avr<=60):
                print("second")
            else:
                print("third")
grd=Grade()
grd.setData(101,"Srijan",26,67)
grd.viewData()
grd.evalGrade()