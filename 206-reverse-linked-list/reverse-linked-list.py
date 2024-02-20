# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        curr = head
        nums = []
        while curr:
            nums.append(curr.val)
            curr = curr.next
        nums = nums[::-1]
        nodes = []
        for num in nums:
            new_node = ListNode(num)
            nodes.append(new_node)
        for idx, node in enumerate(nodes):
            if idx != len(nodes) - 1:
                node.next = nodes[idx+1]
        return nodes[0]