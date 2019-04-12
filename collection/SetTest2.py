#invoking set with constructor
mySet=set({"Apple","Grapes","Apple"})
print(mySet)

thisSet=frozenset({"Apple","Grapes","Apple"}) #will become readonly set
mySet.add("Orange")
print (mySet)
