#dictonary example
dict = {'Name': 'Aditya', 
        'Age': 10, 
        'Class': '5',
        'School':'HPS'}

print ("Dict['Name']:%s"%(dict['Name']))   # reading the value with reference to key 'Name' is a key
print ("dict['Age']: ", dict['Age'])       # 'Age' is a key       
print ("dict['School']: ", dict['School']) # 'School' is a key called from  "dict" object
print (dict)  # show all properties of the dictionary
dict.clear()  # clear all entries
print("after clear ",dict)
dict.update({'city':input(" Your City")})  # add new element to dictionary
print (dict)
del dict       # removes the object of dictionary
print ("After delete")
print (dict)