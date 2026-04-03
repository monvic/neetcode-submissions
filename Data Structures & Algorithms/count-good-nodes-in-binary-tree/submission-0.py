# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def gN(root, m):
            if not root:
                return 0
            
            cr = gN(root.left, max(m, root.val))
            cl = gN(root.right, max(m, root.val))
            s = cr+cl

            if root.val >= m:
                return s+1
            else:
                return s
        
        return gN(root, root.val)

        