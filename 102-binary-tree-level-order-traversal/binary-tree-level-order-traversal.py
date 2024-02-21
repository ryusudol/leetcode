from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return None
        ans = []
        queue = deque()
        queue.append((0, root))
        prev_level = 0
        same_level_elements = []
        while queue:
            curr_level, curr_v = queue.popleft()
            if curr_level != prev_level:
                ans.append(same_level_elements)
                same_level_elements = []
                prev_level = curr_level
            same_level_elements.append(curr_v.val)
            if curr_v.left:
                queue.append((curr_level + 1, curr_v.left))
            if curr_v.right:
                queue.append((curr_level + 1, curr_v.right))
        ans.append(same_level_elements)
        return ans