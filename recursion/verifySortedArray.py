def sortArray(arr, index=0):
   if index==len(arr)-1:
      return True
   if arr[index]>arr[index+1]:
      return False
   return sortArray(arr,index+1)

print(sortArray([1,2,3,4]))
print(sortArray([1,4,10, 15,3]))
print(sortArray([1,4,5,13,18,100,250,320,700]))
