def linSearch(arr, target, index=0):
   if (index>=len(arr)):
      return -1
   if (arr[index]==target):
      return index
   return linSearch(arr, target, index+1)



print(linSearch([1,2,3,4], 2))
print(linSearch([1,2,3,4], 7))
print(linSearch([1,2,3,4, 13, 19, 20, 31], 13))
