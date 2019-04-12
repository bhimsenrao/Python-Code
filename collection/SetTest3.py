# using set operations     union,  intersect,  minus
person1 =set({"Chiru","Naag","venky"})
person2 =set({"venky","NTR","Balaiah"})
person3=set({"NTR","Charan","Ram"})
heroes=person1.union(person2)  # add elements of person1, person2  to heroes 
print(heroes)
heroes=heroes.union(person3)   # add elements of person3 to heroes
print(heroes)
#Other way of using union 
data = person1|person2|person3
print(data)

# intersect sets  , returns only common elements between two or more sets
print(person1.intersection(person2))
print(person1.intersection(person2.intersection(person3)))

#minus returns only elements available with left side set but not right side
print(person1-person2)


