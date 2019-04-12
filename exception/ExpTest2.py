try:
    fh =open("testfile.txt", "r")
    try:
        #fh.write("This is my test file for exception handling!!")
        content = fh.read()
        print( content)
        print("-----")
    except IOError as e:
            print (e)
  # print ("\nError: cannot find file or read data")
    finally:
        fh.close()
        print( "File closed")
except Exception as e:
    print("Error :",e.args)
else:
    print ("done")   