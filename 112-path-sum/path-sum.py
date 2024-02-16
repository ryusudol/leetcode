from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        total_sum = 0
        queue = deque()
        queue.append((root, total_sum))
        while queue:
            curr_v, curr_sum = queue.popleft()
            curr_sum = curr_sum + curr_v.val
            if curr_v.left:
                queue.append((curr_v.left, curr_sum))
            if curr_v.right:
                queue.append((curr_v.right, curr_sum))
            if not curr_v.left and not curr_v.right and curr_sum == targetSum:
                return True
        return False