class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class LinkedList:

    def __init__(self):
        self.head = None
        self.tail= None
        self.size = 0
        
    def getNode(self, index: int) -> Node:
        curr=0
        node = self.head
        while curr != index and node != None:
            node = node.next
            curr+=1
        return node

    def get(self, index: int) -> int:
        if self.size < index:
            return -1
        node = self.getNode(index)
        if node == None:
            return -1
        return node.value

    def addAtHead(self, val: int) -> None:
        newHead = Node(val)
        if self.head == None:
            self.head = newHead
            self.tail = newHead
        else:
            currHead = self.head
            currHead.prev = newHead
            self.head = newHead
            newHead.prev= None
            newHead.next = currHead
        self.size+=1
        

    def addAtTail(self, val: int) -> None:
        newTail = Node(val)
        if self.tail == None:
            self.head = newTail
            self.tail = newTail
        else:
            currTail = self.tail
            currTail.next = newTail
            self.tail = newTail
            newTail.prev= currTail
            newTail.next = None
        self.size+=1

    def deleteAtIndex(self, index: int) -> None:
        if self.size <= index:
            return
        currNode = self.getNode(index)
        if index==0 and self.size==1:
            self.head = None
            self.tail= None
        elif index==0:
            self.head = currNode.next
            self.head.prev = None
        elif index==self.size-1:
            self.tail = currNode.prev
            self.tail.next = None
        else:
            currNode.prev.next=currNode.next
            currNode.next.prev= currNode.prev
        self.size -=1

class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        count=0
        studentsLL=LinkedList()
        sandwichesLL=LinkedList()
        for i in students:
            studentsLL.addAtTail(i)
        for x in sandwiches:
            sandwichesLL.addAtTail(x)
        curr=studentsLL.head
        while(count<studentsLL.size):
            if studentsLL.head.value==sandwichesLL.head.value:
                studentsLL.deleteAtIndex(0)
                sandwichesLL.deleteAtIndex(0)
                count=0
            else:
                count+=1
                studentHead=studentsLL.head
                studentsLL.deleteAtIndex(0)
                studentsLL.addAtTail(studentHead.value)
        return studentsLL.size

