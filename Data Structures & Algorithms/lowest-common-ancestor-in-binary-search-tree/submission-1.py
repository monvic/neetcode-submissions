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
            
            c = root.val == p.val or root.val == q.val
            l = lca(root.left, p, q)
            r = lca(root.right, p, q)

            if (l and r) or (c and r) or (l and c):
                return root
            if l:
                return l
            if r:
                return r
            if c:
                return root
            
            # print (root.val, p.val, q.val)
            return None
        
        result = lca(root, p, q)
        # print(result)
        return result