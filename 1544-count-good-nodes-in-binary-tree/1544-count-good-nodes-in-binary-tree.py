# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # Better Approach
        def dfs(node, largest):
            if not node:
                return 0
            add = 1 if node.val >= largest else 0
            largest = max(largest, node.val)
            return add + dfs(node.left, largest) + dfs(node.right, largest)
        return dfs(root, -10000)

        # My First Approach
        # count = 1
        # def dfs(nums, node):
        #     nonlocal count
        #     if not node:
        #         return
        #     _nums = nums[:]
        #     if all(num <= node.val for num in _nums):
        #         _nums.append(node.val)
        #         count += 1
        #     dfs(_nums, node.left)
        #     dfs(_nums, node.right)
        # dfs([root.val], root.left)
        # dfs([root.val], root.right)
        # return count