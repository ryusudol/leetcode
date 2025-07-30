# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        ans = []
        prev_level, level = 0, []
        queue = deque([(0, root)])
        while queue:
            cur_level, cur_node = queue.popleft()
            if prev_level != cur_level:
                ans.append(level)
                level = []
                prev_level = cur_level
            level.append(cur_node.val)
            if cur_node.left:
                queue.append((cur_level + 1, cur_node.left))
            if cur_node.right:
                queue.append((cur_level + 1, cur_node.right))
        if level:
            ans.append(level)
        return ans