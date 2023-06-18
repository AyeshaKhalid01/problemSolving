def bS(arr, target, start, end):
    if start>end:
        return -1
    m = start + ((end-start)//2)
    if (arr[m]==target):
        return m
    if target<arr[m]:
        return bS(arr,target,start, m-1)
    return bS(arr,target,m+1, end)
