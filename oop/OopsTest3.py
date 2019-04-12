class PolyTest:
    def addNumbers(self,a,b):
        return (a+b)
    def addNumbers(self,a,b,c=0):
        sum=a+b+c
        
        return sum
pt = PolyTest()
print(pt.addNumbers(10,20))
print(pt.addNumbers(10,20,30))
