def mergeSort(input, start, end):
    if start < end:
        mid=(start+end)//2
        mergeSort(input, start, mid)
        mergeSort(input, mid+1, end)
        merge(input, start, mid, end)

def merge(input, start, mid, end):
    temp=[0]*(end-start+1)
    i=start
    j=mid+1
    k=0
    while(i<=mid and j<=end):
        if input[i]<=input[j]:
            temp[k]=input[i]
            i+=1
        else:
            temp[k]=input[j]
            j+=1
        k+=1
    while(i<=mid):
        temp[k]=input[i]
        i+=1
        k+=1
    while(j<=end):
        temp[k]=input[j]
        j+=1
        k+=1
    for i in range(start,end+1):
        input[i]= temp[i-start]

