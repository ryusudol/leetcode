class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        ans, pos, neg = [], [], []
        for num in nums:
            if num > 0: pos.append(num)
            else: neg.append(num)
        print(pos)
        for i in range(int(len(nums)/2)):
            ans.append(pos[i])
            ans.append(neg[i])
        return ans