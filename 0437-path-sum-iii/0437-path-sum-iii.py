# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        def dfs(node, nums):
            if not node:
                return 0
            _nums = nums[:]
            _nums.append(node.val)
            add = 0
            for i in range(len(_nums)):
                if sum(_nums[i:]) == targetSum:
                    add += 1
            return add + dfs(node.left, _nums) + dfs(node.right, _nums)
        return dfs(root, [])