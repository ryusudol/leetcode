# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        cur_level = -1
        values = []
        queue = deque()
        queue.append((0, root))
        while queue:
            level, node = queue.popleft()
            if cur_level != level:
                cur_level = level
                values.append(node.val)
            if node.right:
                queue.append((level + 1, node.right))
            if node.left:
                queue.append((level + 1, node.left))
        return values