num=2
mySet=set({})
#while num>0:
print("Inner Loop ")
for i in range(1,num+1):
    name=input("Enter data")
    if(len(name)>5):
        mySet.add(name)
    #print( mySet)
    #print ("------")
#num=num-1
    #mySet.clear()
print ("End of Loop") 
print(mySet)