# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    result = 0
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        def calcResult(root):
            if root == None:
                return 0
            
            lHeight = calcResult(root.left)
            rHeight = calcResult(root.right)

            self.result = max(self.result, lHeight+rHeight)
            return 1+max(lHeight,rHeight)
        
        calcResult(root)
        return self.result
        