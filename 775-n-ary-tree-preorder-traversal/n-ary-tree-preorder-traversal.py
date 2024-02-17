"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        if not root:
            return []
        visited = []
        visited.append(root.val)
        for v in root.children:
            visited += self.preorder(v)
        
        return visited