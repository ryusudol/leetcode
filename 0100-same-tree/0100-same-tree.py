# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # BFS
        # if (not p and q) or (p and not q):
        #     return False
        # elif not p and not q:
        #     return True

        # queue_p, queue_q = deque([('c', 0, p)]), deque([('c', 0, q)])
        # while queue_p and queue_q:
        #     pos_p, cur_level_p, cur_p = queue_p.popleft()
        #     pos_q, cur_level_q, cur_q = queue_q.popleft()

        #     if pos_p != pos_q or cur_level_p != cur_level_q or cur_p.val != cur_q.val:
        #         return False

        #     if cur_p.left:
        #         queue_p.append(('l', cur_level_p + 1, cur_p.left))
        #     if cur_q.left:
        #         queue_q.append(('l', cur_level_q + 1, cur_q.left))
        #     if cur_p.right:
        #         queue_p.append(('r', cur_level_p + 1, cur_p.right))
        #     if cur_q.right:
        #         queue_q.append(('r', cur_level_q + 1, cur_q.right))
        # return queue_p == queue_q

        # DFS
        if not p and not q:
            return True
        elif not p or not q:
            return False
        elif p.val != q.val:
            return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)