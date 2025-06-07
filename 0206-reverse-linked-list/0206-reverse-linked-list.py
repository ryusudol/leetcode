# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Better Approach with 3 pointers
        p, q, r = head, None, None
        while p:
            r = q
            q = p
            p = p.next
            q.next = r
        return q

        # My First Approach
        # if not head or not head.next:
        #     return head
        # nodes = []
        # cur = head
        # while cur:
        #     nodes.append(cur)
        #     cur = cur.next
        # for i in range(len(nodes) - 1):
        #     nodes[-1 - i].next = nodes[-2 - i]
        # head.next = None
        # return nodes[-1]