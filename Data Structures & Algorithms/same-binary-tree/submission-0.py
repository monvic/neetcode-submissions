# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        print(p,q)
        if p == None and q == None:
            return True
        elif (p == None and q != None) or (q == None and p != None):
            return False
        elif p.val != q.val:
            return False
        else:
            lSame = self.isSameTree(p.left, q.left)
            rSame = self.isSameTree(p.right, q.right)
            return (lSame and rSame and (p.val == q.val))

        