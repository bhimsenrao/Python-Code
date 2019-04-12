# display reverse value of the given number

num =int(input("Enter number"))
rev=0
temp=num

while(temp>0):
    rev=rev*10+ temp%10
    temp=temp//10
#   temp=int(temp/10)    
print("reversed value %d"%rev)    

#  dry run of the program
#      Num        temp    temp%10          rev*10+ temp%10        temp=temp//10
#      4567       4567      7                0*10 +7                   4567//10=456
#      4567        456      6                7*10+6                     456//10=45       
#                   45      5                76*10+5                     45//10=4
#                    4      4                765*10+4                     4//10=0


