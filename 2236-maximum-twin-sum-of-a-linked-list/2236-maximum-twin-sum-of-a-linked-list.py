# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        nums = []
        cur = head
        while cur:
            nums.append(cur.val)
            cur = cur.next
        max_sum = 0
        for i in range(len(nums) // 2):
            max_sum = max(nums[i] + nums[-1 - i], max_sum)
        return max_sum