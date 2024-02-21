from collections import deque
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return None
        ans = []
        queue = deque()
        queue.append((0, root))
        prev_level = 0
        same_level_elements = []
        left_to_right = True
        while queue:
            curr_level, curr_v = queue.popleft()
            if prev_level != curr_level:
                if not left_to_right:
                    same_level_elements.reverse()
                ans.append(same_level_elements)
                same_level_elements = []
                prev_level = curr_level
                left_to_right = not left_to_right
            same_level_elements.append(curr_v.val)
            if curr_v.left:
                queue.append((curr_level + 1, curr_v.left))
            if curr_v.right:
                queue.append((curr_level + 1, curr_v.right))
        if not left_to_right:
            same_level_elements.reverse()
        ans.append(same_level_elements)
        return ans