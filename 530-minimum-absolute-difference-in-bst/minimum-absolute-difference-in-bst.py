from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        visited = []
        queue = deque()
        queue.append(root)
        while queue:
            curr_v = queue.popleft()
            visited.append(curr_v.val)
            if curr_v.left:
                queue.append(curr_v.left)
            if curr_v.right:
                queue.append(curr_v.right)
        visited.sort()
        min_diff = 999999
        for idx, num in enumerate(visited):
            if idx != len(visited) - 1:
                curr_diff = visited[idx+1] - num
                min_diff = min(min_diff, curr_diff)
        return min_diff