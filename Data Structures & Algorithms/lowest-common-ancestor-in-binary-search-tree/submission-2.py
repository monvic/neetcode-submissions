# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        def lca(root: TreeNode, p: TreeNode, q: TreeNode):
            if root == None:
                return None
            
            if root.val == p.val or root.val == q.val:
                return root
            l = lca(root.left, p, q)
            r = lca(root.right, p, q)

            if (l and r):
                return root
            if l:
                return l
            if r:
                return r
            
            # print (root.val, p.val, q.val)
            return None
        
        result = lca(root, p, q)
        # print(result)
        return result