#fo = open("myFile.txt", "w")
fo = open("myFile.txt", "a")
message=input("Enter message")
fo.write(message+"\n")
#fo.write("my text\n")
# Close opend file
fo.close()


