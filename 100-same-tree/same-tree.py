from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p or not q:
            return p == q
        queue1, queue2 = deque(), deque()
        queue1.append(p)
        queue2.append(q)
        while queue1 and queue2:
            curr_v1 = queue1.popleft()
            curr_v2 = queue2.popleft()
            if curr_v1 and curr_v2 and curr_v1.val == curr_v2.val:
                queue1.append(curr_v1.left)
                queue1.append(curr_v1.right)
                queue2.append(curr_v2.left)
                queue2.append(curr_v2.right)
            elif curr_v1 is None and curr_v2 is None:
                pass
            else:
                return False
        return queue1 == queue2