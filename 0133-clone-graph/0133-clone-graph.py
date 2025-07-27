"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        
        old_to_new = {}

        def dfs(original_node):
            if original_node in old_to_new:
                return old_to_new[original_node]
            
            clone_node = Node(original_node.val)
            old_to_new[original_node] = clone_node

            if original_node.neighbors:
                for original_neighbor in original_node.neighbors:
                    clone_node.neighbors.append(dfs(original_neighbor))
            
            return clone_node
        
        return dfs(node)