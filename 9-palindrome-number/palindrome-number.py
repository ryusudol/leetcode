class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        str_x = str(x)
        str_x_list = list(str_x)
        left, right = 0, len(str_x_list) - 1
        while left <= right:
            if str_x_list[left] != str_x_list[right]:
                return False
            left += 1
            right -= 1
        return True