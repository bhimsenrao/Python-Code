class Test:
   x=None
   def storeData(self,y):
        self.x=y
   def viewData(self):
        print(self.x)
  
t= Test()
t.storeData(10)
t.viewData()