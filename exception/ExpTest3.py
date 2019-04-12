try:
   fh = open("ExpTest1.py", "r")
   try:
      print(fh.read())
   #except Exception as e:
   #   print(e)
   finally:
      print ("Going to close the file")
      fh.close()
except IOError:
   print ("Error: can\'t find file or read data")
   