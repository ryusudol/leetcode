# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        seq1, seq2 = [], []
        def dfs(seq, node):
            if not node:
                return
            if not node.left and not node.right:
                seq.append(node.val)
            dfs(seq, node.left)
            dfs(seq, node.right)
        dfs(seq1, root1)
        dfs(seq2, root2)
        return seq1 == seq2