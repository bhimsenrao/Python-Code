# Open a file
fo = open("testFile.txt", "r")
lines =fo.readlines()
word=raw_input("Search word")
for line in lines:
    x=line.split(" ")
    for w in range(len(x)):
        if word==x[w] :
            print line
fo.close()