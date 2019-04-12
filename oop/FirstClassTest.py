class TestMe:
    slno=101
    name="Raju"
    def setData(self,sln,sname):
        self.slno=sln
        self.name=sname

    def viewData(self):
        print ("Slno=%d name=%s"%(self.slno,self.name))
class CreditCardData:
    cardNo=None
    def inputCard(self,ccNo):
        self.cardNo=ccNo
    def showCard(self):
        return self.cardNo    
    