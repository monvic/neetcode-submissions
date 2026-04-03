# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    result = []
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        def inOrder(root):
            if root == None:
                return
            inOrder(root.left)
            result.append(root.val)
            inOrder(root.right)

        inOrder(root)
        return result

 

        