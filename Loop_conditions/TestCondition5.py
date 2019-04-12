num=int(input("Three digit numer"))
if(num>999 or num<100):
    print("required three digit only")
else:
    print(num%10, int(num/100))
    if(num%10==int(num/100)):
        print("Palindrom")
    else:
        print("Non palindrom")