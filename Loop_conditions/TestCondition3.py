x= int( input("Stdcode"))
y= int( input("Zone Ex:1,2,3,4"))

if x>=1 and x<=40:
    if y==1:
         print("North")
         print("Testing")
    elif y==2:
        print("South")
    else:
        print("Unknown Zone")
else:            
    print("Other location")