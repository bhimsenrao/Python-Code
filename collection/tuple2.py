#tuple program 2
lst=("sunday","monday","tuesday","wednesday",
     "thursday","friday","saturday");
for day in lst[0:3] :
  print (day)
# print specific range
print (lst[1:4])
print (lst[3:])
print ("value from given index:",lst[0])
print ("Length of the array : %d"%(len(lst)))
del lst
# you will get error if you print after delete   ---- print lst