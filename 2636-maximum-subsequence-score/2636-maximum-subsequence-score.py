class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        pairs = list(zip(nums2, nums1))
        pairs.sort(reverse=True)
        total, max_score = 0, 0
        heap = []
        for pair in pairs:
            heappush(heap, pair[1])
            total += pair[1]
            if len(heap) == k:
                max_score = max(max_score, pair[0] * total)
                total -= heappop(heap)
        return max_score