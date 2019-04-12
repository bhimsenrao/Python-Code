f=open("datafile.cvs","r")

for line in f.readlines():
    data=line.split(',')
    #print(data)
    if(line.count('manager')==1):
        for field in range(len(data)):
            print(data[field], end=' ')
        print()
