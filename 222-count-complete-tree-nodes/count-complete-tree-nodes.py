from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
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
        return len(visited)