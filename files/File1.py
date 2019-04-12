# Open a file
fo = open("MyFile.txt", "r")
fo.close()
if(not fo.closed):
    print ("Filename: ", fo.name)
    print ("File Mode : ", fo.mode)
    print ("Closed Status : ", fo.closed)
else:
    print("File closed")
