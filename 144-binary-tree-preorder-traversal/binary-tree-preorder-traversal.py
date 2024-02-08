from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorder(self, root, visited=[]):
        if root is None:
            return None
        visited.append(root.val)
        self.preorder(root.left, visited)
        self.preorder(root.right, visited)

    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        visited = []
        self.preorder(root, visited)
        return visited