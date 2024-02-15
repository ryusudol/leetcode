# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None or list2 is None:
            return list1 or list2
        nums1, nums2 = [], []
        curr = list1
        while curr:
            nums1.append(curr.val)
            curr = curr.next
        curr = list2
        while curr:
            nums2.append(curr.val)
            curr = curr.next
        nums1.sort(reverse=True)
        nums2.sort(reverse=True)
        nodes = []
        while nums1 and nums2:
            if nums1[-1] <= nums2[-1]:
                target = nums1.pop()
            else:
                target = nums2.pop()
            new_node = ListNode(target)
            nodes.append(new_node)
        if nums1:
            while nums1:
                target = nums1.pop()
                new_node = ListNode(target)
                nodes.append(new_node)
        elif nums2:
            while nums2:
                target = nums2.pop()
                new_node = ListNode(target)
                nodes.append(new_node)
        for idx, node in enumerate(nodes):
            if idx != len(nodes) - 1:
                node.next = nodes[idx+1]
        return nodes[0]