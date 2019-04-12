# looping program using python

count=int(input("Number="))
if count>=10:
    print("Limit exceeded")
else:    
    while (count<10):
        count=count+1
        print( count)
print ("last count value", count)