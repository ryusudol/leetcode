# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        length = 0
        curr = head
        while curr:
            length += 1
            curr = curr.next
        if length == 0:
            return head
        k = k % length
        print(k)
        for _ in range(k):
            curr = head
            while curr.next.next:
                curr = curr.next
            new_node = ListNode(curr.next.val, head)
            curr.next = None
            head = new_node
        return head
