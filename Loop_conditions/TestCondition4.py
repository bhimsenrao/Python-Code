year=int(input("Enter Year"))
if(year%4==0 or (year%100!=0 and year%400==0 )):
    print("Leap")
else:
    print("Non leap")

# 121