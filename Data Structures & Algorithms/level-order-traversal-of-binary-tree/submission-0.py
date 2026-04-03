# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root == None:
            return []

        q = deque()
        lvl = -1
        q.append((root, 0))
        result = []
        while len(q) > 0:
            lvl += 1
            r = []
            # print(lvl)
            # print(q[0][1], q)
            while q and q[0][1] == lvl:
                (node, _) = q.popleft()
                if node.left:
                    q.append((node.left, lvl+1))
                if node.right:
                    q.append((node.right, lvl+1))
                r.append(node.val)
            
            result.append(r)
        return result