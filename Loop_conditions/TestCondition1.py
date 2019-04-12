# python 2.x version input used as raw_input()
# python 3.x version input as input()

x=input("Enter Number")
print(float(x)/2.0)

print(float(x)%2.0)

if float(x)%2==0:
    print("Even")
else:
    print("Odd")