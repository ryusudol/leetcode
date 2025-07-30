# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        # Better Approach
        return [root.val] + self.preorderTraversal(root.left) + self.preorderTraversal(root.right)

        # My First Approach
        # def dfs(node, visited):
        #     if not node:
        #         return
        #     visited.append(node.val)
        #     dfs(node.left, visited)
        #     dfs(node.right, visited)
        
        # ans = []
        # dfs(root, ans)
        # return ans