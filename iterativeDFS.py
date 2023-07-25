#post order
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        final=[]
        stack=[root]
        visited=[False]
        while stack:
            curr=stack.pop()
            visit=visited.pop()
            if curr:
                if visit:
                    final.append(curr.val)
                else:
                    stack.append(curr)
                    visited.append(True)
                    if curr.right:
                        stack.append(curr.right)
                        visited.append(False)
                    if curr.left:
                        stack.append(curr.left)
                        visited.append(False)
        return final

