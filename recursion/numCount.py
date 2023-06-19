def numCount(arr, target, index=0, returnLis=None):
   if returnLis==None:
      returnLis=[]
   if index>=len(arr):
      return returnLis
   if arr[index]==target:
      returnLis.append(index)
   return numCount(arr, target, index+1, returnLis)

print(numCount([1,2,4,4], 4))
print(numCount([1,2,3,4], 2))
print(numCount([1,2,3,4, 13, 19, 20, 31], 13))
print(numCount([1,2,3,4], 5))
