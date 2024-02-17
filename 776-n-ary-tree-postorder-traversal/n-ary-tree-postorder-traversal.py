"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        if not root:
            return []
        visited = []
        for v in root.children:
            visited += self.postorder(v)
        visited.append(root.val)
        return visited