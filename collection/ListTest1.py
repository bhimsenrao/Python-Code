#-- List with values

lst=["Apple","Mango","guava","orange"]  # setting default values in list
lst.append("Banana")                    # add new element
lst.sort()
lst.insert(1,"grapes")                  #insert at a specific location 
lst.pop()
for i in range(len(lst)):      
    print(lst[i], end =" ")
print()
print("Min value=",min(lst))
print("Max value=",max(lst))
lst1=["sunday","monday","tuesday"]
print(list("hello"))
lst2=lst
print(lst==lst2)
#print(cmp(lst,lst1))