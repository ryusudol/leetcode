# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        min_depth = 999999
        
        def dfs(node, count):
            count += 1
            nonlocal min_depth
            if not node.left and not node.right:
                min_depth = min(min_depth, count)
                return
            if node.left:
                dfs(node.left, count)
            if node.right:
                dfs(node.right, count)

        dfs(root, 0)
        return min_depth