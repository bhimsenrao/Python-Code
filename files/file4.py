# Open a file
fo = open("MyFile.txt", "r")
lines =fo.readlines()
#print(lines)
for i in range(len(lines)):
   print(lines[i])
fo.close()