#loop testing
num=int(input('Enter Number'))
temp=num
count=0
while(temp>0):
    temp=temp//10
    count=count+1
print("count of digits for %d = %d"%(num,count))
