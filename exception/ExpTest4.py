def add_Numbers(var1, var2):
   try:
      return (int(var1)+int(var2))
   except ValueError as arg:
      print (arg)
      return 0

# Call above function here.
print(add_Numbers(12,"A"))