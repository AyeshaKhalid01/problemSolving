def numCount2(arr, target, index=0):
   curr=[]
   if index>=len(arr):
      return curr
   if arr[index]==target:
      curr.append(index)
   all=numCount2(arr, target, index+1)
   curr.extend(all)
   return curr
print(numCount2([1,2,4,4], 4))
#print(numCount([1,2,3,4], 2))
#print(numCount([1,2,3,4, 13, 19, 20, 31], 13))
#print(numCount([1,2,3,4], 5))
