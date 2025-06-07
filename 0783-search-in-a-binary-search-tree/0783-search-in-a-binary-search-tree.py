# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        queue = deque()
        queue.append(root)
        target = None
        while queue:
            cur = queue.popleft()
            if cur.val == val:
                target = cur
                break
            if cur.left:
                queue.append(cur.left)
            if cur.right:
                queue.append(cur.right)
        return target