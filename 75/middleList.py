# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp=head
        length=0
        while temp:
            length+=1
            temp = temp.next
        for i in range(0,length//2):
            head=head.next
        return head
