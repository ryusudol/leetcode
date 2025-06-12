class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        def dfs(node, direction, length):
            if not node:
                return
            nonlocal longest
            longest = max(longest, length + 1)
            dfs(node.left, 'l', 0 if direction == 'l' else length + 1)
            dfs(node.right, 'r', 0 if direction == 'r' else length + 1)
        longest = 0
        dfs(root.left, 'l', 0)
        dfs(root.right, 'r', 0)
        return longest