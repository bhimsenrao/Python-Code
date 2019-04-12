#tuple program 1
lst=("sunday","monday","tuesday","wednesday","thursday","friday","saturday");
#lst.add("one")  add is not the property of tuple
print (lst)
#del lst
print("Values from tuble:")
for i in range(7):
    print(lst[i],end=" ")

print("\nValues from range:")
#other way of using for loop
for i in range(len(lst)):
    print(lst[i],end ="  ")
del lst
#other way of using for loop
print("\nValues from sub-range:")
for day in lst[1:5]:
    print(day, end="  ")
