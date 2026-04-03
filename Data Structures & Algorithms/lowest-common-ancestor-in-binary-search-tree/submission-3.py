# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        def lca(root: TreeNode, p: TreeNode, q: TreeNode):
            if root.val < p.val and root.val < q.val:
                return lca(root.right, p, q)
            elif root.val> p.val and root.val >q.val:
                return lca(root.left, p,q)
            else:
                return root
        
        result = lca(root, p, q)
        return result