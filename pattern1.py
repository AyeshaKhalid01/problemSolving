def pattern1(n):
   for i in range(n):
      for x in range(i):
         print("*", end="")
      print()

pattern1(5)
