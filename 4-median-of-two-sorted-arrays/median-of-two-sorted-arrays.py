class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        arr = nums1 + nums2
        arr.sort()
        half = int(len(arr)/2)
        if len(arr) % 2 == 1:
            return arr[half]
        else:
            avg = (arr[half-1] + arr[half]) / 2
            return avg