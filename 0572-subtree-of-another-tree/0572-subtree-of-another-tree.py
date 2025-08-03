class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        queue = deque([root])
        while queue:
            cur_node = queue.popleft()
            if cur_node.val == subRoot.val:
                is_subroot = True
                root_queue = deque([(0, 'c', cur_node)])
                subroot_queue = deque([(0, 'c', subRoot)])
                while root_queue and subroot_queue:
                    cur_root_level, cur_root_dir, cur_root_node = root_queue.popleft()
                    cur_subroot_level, cur_subroot_dir, cur_subroot_node = subroot_queue.popleft()
                    if cur_root_node.val != cur_subroot_node.val or cur_root_level != cur_subroot_level or cur_root_dir != cur_subroot_dir:
                        is_subroot = False
                        break
                    if cur_root_node.left:
                        root_queue.append((cur_root_level + 1, 'l', cur_root_node.left))
                    if cur_root_node.right:
                        root_queue.append((cur_root_level + 1, 'r', cur_root_node.right))
                    if cur_subroot_node.left:
                        subroot_queue.append((cur_subroot_level + 1, 'l', cur_subroot_node.left))
                    if cur_subroot_node.right:
                        subroot_queue.append((cur_subroot_level + 1, 'r', cur_subroot_node.right))
                if len(root_queue) != len(subroot_queue):
                    is_subroot = False
                if is_subroot:
                    return True
            if cur_node.left:
                queue.append(cur_node.left)
            if cur_node.right:
                queue.append(cur_node.right)
        return False