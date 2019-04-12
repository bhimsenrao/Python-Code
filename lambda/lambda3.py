from functools import reduce
f = lambda a,b: a if (a > b) else b 
print(reduce(f, [47,11,42,102,13]))

a=[1,2,3,4]
def sum(x,y):
    return x+y
b = reduce(sum, a) # b = (((1+2)+3)+4) = 10
print(b)
