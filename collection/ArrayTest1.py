from array import *

arr  =array('i',[10,20,30,50])
print("Default values of the array")
for i in arr:
    print(i,end=" ")
print("\n------------------") 
#----  adding element to an array
#arr.append(40)
arr.insert(3,40)
print("After appending value")
for i in arr:
    print(i,end=" ")
print("\n------------------") 
arr.reverse()                  # reverse the values of the array
arr.insert(2,25)
arr.remove(40)
print("After Reverse value")
for i in arr:
    print(i,end=" ")
print("\n------------------") 
