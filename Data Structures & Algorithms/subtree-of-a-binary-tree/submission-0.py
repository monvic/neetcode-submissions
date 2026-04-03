# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True
        if not root:
            return False

        result = self.isSameTree(root, subRoot)
        if result:
            return True
        else:
            lResult = self.isSubtree(root.left, subRoot)
            rResult = self.isSubtree(root.right, subRoot)
            return lResult or rResult
    
    def isSameTree(self, t1, t2):
        if not t1 and not t2:
            return True
        elif t1 and t2 and t1.val == t2.val:
            return (self.isSameTree(t1.left, t2.left) and self.isSameTree(t1.right,t2.right))
        else:
            return False

        