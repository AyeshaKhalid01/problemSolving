# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if len(inorder)==0:
            return None
        if len(preorder)==0:
            return None
        node = preorder.pop(0)
        index = inorder.index(node)
        node = TreeNode(node)
        node.left=self.buildTree(preorder, inorder[:index])
        node.right=self.buildTree(preorder, inorder[index+1:])
        return node
