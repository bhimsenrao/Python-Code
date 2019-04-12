try:
    x=int(input("numerator: "))
    y=int(input("Denominator: "))
    print ("numerator=",x," denominator=",y)
    z=x/y
    print (z)
except  ZeroDivisionError as e:
    print ("Error:\n %s"%(e))
except  Exception as e1:
    print ("Error:\n %s"%(e1))    
else:
    print ("Successfully completed")
finally:
    print ("Program ended")