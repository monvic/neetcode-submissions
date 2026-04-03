# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        depth = -1
        def rightSide(root, d, depth, result):
            if not root:
                return d-1
            
            if d>depth:
                result.append(root.val)
            
            dr = max(depth, rightSide(root.right, d+1, depth, result))
            dl = max(depth, rightSide(root.left, d+1, dr, result))
            return max(dr, dl)
        
        rightSide(root, 0, depth, result)
        return result