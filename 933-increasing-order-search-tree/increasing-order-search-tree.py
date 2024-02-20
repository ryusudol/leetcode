# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        def dfs(node, visited=[]):
            if not node:
                return None
            dfs(node.left)
            visited.append(node.val)
            dfs(node.right)
            return visited
        visited = dfs(root)
        visited.sort()
        prev = head_node = TreeNode(visited[0])
        for i in range(1, len(visited)):
            new_node = TreeNode(visited[i])
            prev.right = new_node
            prev = new_node
        return head_node