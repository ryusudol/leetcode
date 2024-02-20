from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        visited = []
        queue = deque()
        queue.append(root)
        while queue:
            curr_v = queue.popleft()
            if low <= curr_v.val <= high: visited.append(curr_v.val)
            if curr_v.left: queue.append(curr_v.left)
            if curr_v.right: queue.append(curr_v.right)
        return sum(visited)