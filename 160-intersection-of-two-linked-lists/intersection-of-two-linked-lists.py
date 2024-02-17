# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        curr_A, curr_B = headA, headB
        memo_A, memo_B = {}, {}
        while curr_A or curr_B:
            if curr_A not in memo_A:
                memo_A[curr_A] = True
            if curr_B not in memo_B:
                memo_B[curr_B] = True
            if curr_A in memo_B:
                return curr_A
            if curr_B in memo_A:
                return curr_B
            if curr_A:
                curr_A = curr_A.next
            if curr_B:
                curr_B = curr_B.next
        return None
