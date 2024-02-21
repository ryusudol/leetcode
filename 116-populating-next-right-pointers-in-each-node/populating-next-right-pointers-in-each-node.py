"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
from collections import deque
class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return None
        nums = []
        queue = deque()
        queue.append((0, root))
        while queue:
            curr_level, curr_v = queue.popleft()
            nums.append((curr_level, curr_v.val))
            if curr_v.left:
                queue.append((curr_level + 1, curr_v.left))
            if curr_v.right:
                queue.append((curr_level + 1, curr_v.right))
        nums.pop(0)
        prev_level, prev_node = 0, None
        queue.append((prev_level, root))
        while queue:
            curr_level, curr_v = queue.popleft()
            if prev_level != curr_level:
                prev_node.next = None
                prev_level = curr_level
            elif prev_node:
                prev_node.next = curr_v
            prev_node = curr_v
            if curr_v.left: queue.append((curr_level + 1, curr_v.left))
            if curr_v.right: queue.append((curr_level + 1, curr_v.right))
            if not queue: curr_v.next = None
        return root