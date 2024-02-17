from collections import deque
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if not root:
            return 0
        max_depth = 0
        queue = deque()
        queue.append((root, 1))
        while queue:
            curr_v, curr_depth = queue.popleft()
            max_depth = max(max_depth, curr_depth)
            for v in curr_v.children:
                queue.append((v, curr_depth + 1))
        return max_depth