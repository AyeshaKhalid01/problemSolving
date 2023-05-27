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


x=[2,3,5,1,9,7, 10]
mergeSort(x, 0, len(x)-1)
print(x)

class Node:
    def __init__(self, data):
        self.data=data
        self.next=None

class LinkedList:
    def __init__(self,head):
        self.head = head

    def linkedListReversal(self, head):
        if (head == None or head.next == None):
            return head
        newHead = self.linkedListReversal(head.next)
        head.next.next=head
        head.next=None
        self.head=newHead
        return self.head

    def reverseLoop(self,head):
        prev = None
        curr = head
        print(curr.data)
        while (curr != None and curr.next != None):
            tempNext = curr.next
            curr.next = prev
            prev = curr
            curr = tempNext
        return curr

n1=Node(1)
n2=Node(2)
n3=Node(3)
n1.next = n2
n2.next = n3
x=LinkedList(n1)
x.linkedListReversal(n1)
print(n2.next.data)
print(x.head.data)
print(x.reverseLoop(n3).data)

