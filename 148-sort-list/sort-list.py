# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return None
        vals = []
        curr = head
        while curr:
            vals.append(curr.val)
            curr = curr.next
        vals.sort()
        nodes = []
        for val in vals:
            new_node = ListNode(val)
            nodes.append(new_node)
        for idx, node in enumerate(nodes):
            if idx != len(nodes) - 1:
                node.next = nodes[idx + 1]
        return nodes[0]