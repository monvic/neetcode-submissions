# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def valid(root, left, right):
            if root == None:
                return True
            
            if root.val <= left or root.val >= right:
                return False
            
            l_valid = valid(root.left, left, root.val)
            r_valid = valid(root.right, root.val, right)

            return l_valid and r_valid
        return valid(root, float("-inf"), float("+inf"))
        