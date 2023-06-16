def pattern1(n):
   for i in range(1,2*n):
      if i<n:
         temp = i
      else:
         temp=n-(i-n)
      for x in range(temp):
         print("*", end="")
      print()

pattern1(5)
