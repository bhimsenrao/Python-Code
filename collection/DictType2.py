myrecord={}
myset=set({"Apple","Grapes","Banana"})
myrecord['id']=11
print(myrecord)
myrecord['name']="Aman"
myrecord['location']="Hyderabad"
myrecord['country']="India"

myrecord['fruits']=myset   # adding set as sublist element of dictionary
print(myrecord)
print(myrecord['id'])

del myrecord['location']
print(myrecord)
myfrs =myrecord['fruits']
print(myfrs)
myfrs.remove('Grapes')
myrecord['fruits']=myset   # adding set as sublist element of dictionary
print(myrecord)
