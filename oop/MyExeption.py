#creating user defined exception
class AgeValidationException(Exception):
    pass
#------------------------- separate class that class function     
class  UserData:
    def validateAge(self,age):
        try:
            if(age<18):
                raise AgeValidationException("Invalid age")
            else:
                print("valid age")
        except AgeValidationException as a:
            print(a)    
#--------------------------- execute class here
ud= UserData()
age=int(input("enter Age"))
ud.validateAge(age)