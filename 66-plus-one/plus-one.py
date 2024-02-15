class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num_str = ''
        for digit in digits:
            num_str += str(digit)
        num_str = int(num_str) + 1
        num_str = str(num_str)
        ans = []
        for digit in num_str:
            ans.append(int(digit))
        return ans