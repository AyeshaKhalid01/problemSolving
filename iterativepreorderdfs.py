# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack=[]
        final=[]
        curr=root
        while curr or stack:
            if curr:
                final.append(curr.val)
                if curr.right:
                    stack.append(curr.right)
                curr=curr.left
            else:
                curr=stack.pop()
        return final
