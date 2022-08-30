# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if (head == None) or (head.next == None):
            return head
        temp = head.val
        temp2 = head.next.next
        head.val = head.next.val
        head.next.val = temp
        head.next.next = self.swapPairs(temp2)
        return head
                
