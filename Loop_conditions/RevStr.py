# reverse string 
name =input("Enter Name: ")
rev=""
nameLen=len(name)
ch=input("search character: ")
print("---------")
cnt=0
while nameLen>0:
     if(name[nameLen-1]==ch):
          cnt+=1

     rev=rev+name[nameLen-1]
     nameLen=nameLen-1
print ("reverse =",rev) 
print("--------")
print(ch," repeated for ",cnt," times")
#----------------------------------------------------------------


# write your code to reverse the string value
str1=""
slen=len(str)-1
while(slen>=0):
     print(str[slen],end='')
     str1=str1+str[slen]
     slen=slen-1
print("\n",str1)     
