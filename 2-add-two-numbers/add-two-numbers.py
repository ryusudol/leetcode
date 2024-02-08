# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1 = []
        num2 = []
        curr = l1
        while curr is not None:
            num1.append(curr.val)
            curr = curr.next
        curr = l2
        while curr is not None:
            num2.append(curr.val)
            curr = curr.next
        num1.reverse()
        num2.reverse()
        num1_str = ''.join(str(num) for num in num1)  # Due to 'join' method, the time complexity can decrease a lot.
        num2_str = ''.join(str(num) for num in num2)
        res = int(num1_str) + int(num2_str)
        res = list(str(res))
        res.reverse()
        prev = None
        first = None
        for el in res:
            new_node = ListNode(el)
            if not first:
                first = new_node
            if prev:
                prev.next = new_node
            prev = new_node
        return first