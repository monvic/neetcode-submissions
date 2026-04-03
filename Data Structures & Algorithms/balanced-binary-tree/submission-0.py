# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    result = True
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

       
        def heightCalc(root):
            if root == None:
                return 0

            lHeight = heightCalc(root.left) 
            rHeight = heightCalc(root.right)

            if abs(lHeight-rHeight)>1:
                self.result = False
            
            h = 1+max(lHeight,rHeight)
            return h

        heightCalc(root)
        return self.result
        
        

        