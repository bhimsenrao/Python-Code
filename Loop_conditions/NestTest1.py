
rows=4
i=1
col=1
while(i<=rows):
    while(col<=i):
        print(" X ",end="")
        col=col+1
    i=i+1
    col=1
    print("")

#  dry run
# rows=4    i=1   col=1
#  i<=rows       i=1
#       col<=i   1<=1     X  col=col+1  =2   2<>1
#     i=i+1   i=2  col=1        