thisSet={"Apple","Grapes","Apple"}
for f in thisSet:
    print(f, end =" ")

print("\n-----")
#adding element to SET
thisSet.add(input("New Value to Set ")) 
print(thisSet)
# making duplicate copy of Set
newSet= thisSet.copy()
print(newSet)
thisSet.clear()  # remove all entries from 'thisSet'  by using clear() method
print(thisSet)
newSet.remove("Apple")  # delete element from newSet
print(newSet)
