# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        if not root.left and not root.right:
            return 1
        cur_level, max_sum_level = 1, 1
        total, max_total = 0, root.val
        queue = deque()
        queue.append((cur_level, root))
        while queue:
            level, node = queue.popleft()
            if cur_level != level:
                max_sum_level = cur_level if total > max_total else max_sum_level
                max_total = max(max_total, total)
                cur_level = level
                total = node.val
            else:
                total += node.val
            if node.left:
                queue.append((level + 1, node.left))
            if node.right:
                queue.append((level + 1, node.right))
        return cur_level if total > max_total else max_sum_level