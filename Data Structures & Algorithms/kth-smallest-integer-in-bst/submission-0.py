# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    result = 0
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        def kSmall(root, count):
            if root == None:
                return count
            count = kSmall(root.left, count)
            print(count, root.val)
            if count == 1:
                self.result = root.val
                print(self.result)
            count -= 1
            count = kSmall(root.right, count)
            return count
        result = kSmall(root, k)
        return self.result
    
        
        