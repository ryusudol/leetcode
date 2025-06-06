# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head.next:
            return None
        left = head
        right = head
        prev = None
        while right and right.next:
            right = right.next.next
            prev = left
            left = left.next
        prev.next = left.next
        return head