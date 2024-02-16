# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        max_depth = 0
        def dfs(start, count):
            if start is None:
                return
            nonlocal max_depth
            count += 1
            max_depth = max(max_depth, count)
            dfs(start.left, count)
            dfs(start.right, count)
        dfs(root, max_depth)
        return max_depth