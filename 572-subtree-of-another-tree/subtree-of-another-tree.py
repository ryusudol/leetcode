from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def isTreeSame(node1, node2):
            if not node1 and not node2:
                return True
            elif not node1 or not node2:
                return False
            elif node1.val != node2.val:
                return False
            return isTreeSame(node1.left, node2.left) and isTreeSame(node1.right, node2.right)

        queue = deque()
        queue.append(root)
        while queue:
            curr_v = queue.popleft()
            if curr_v.val == subRoot.val and isTreeSame(curr_v, subRoot):
                return True
            if curr_v.left:
                queue.append(curr_v.left)
            if curr_v.right:
                queue.append(curr_v.right)
        return False