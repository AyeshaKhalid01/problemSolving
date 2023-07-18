def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        currSum=sum(arr[:k-1])
        num=0
        for i in range(len(arr)-k+1):
            print(i)
            currSum+=arr[i+k-1]
            if (currSum)//k>=threshold:
                #print(arr[i:i+k], currSum, (currSum)//k)
                num+=1
            #print(1, currSum)
            currSum-=arr[i]
            #print(2, currSum)
        return num


