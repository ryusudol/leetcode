# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # DFS
        # if not root:
        #     return 0
        # left_depth = self.maxDepth(root.left)
        # right_depth = self.maxDepth(root.right)
        # return max(left_depth, right_depth) + 1

        # BFS
        if not root:
            return 0
        max_depth = 1
        queue = deque()
        queue.append((max_depth, root))
        while queue:
            max_depth, node = queue.popleft()
            if node.left:
                queue.append((max_depth + 1, node.left))
            if node.right:
                queue.append((max_depth + 1, node.right))
        return max_depth