# Open a file
fo = open("testFile.txt", "r+")
str = fo.read(11);
print ("Read String is : ", str)

# Check current position
position = fo.tell();
print( "Current file position : ", position)
str = fo.read(15);
print (str)
# Reposition pointer at the beginning once again
position = fo.seek(0, 1);
str = fo.read(10);
print ("Again read String is : ", str)
# Close opend file
fo.close()