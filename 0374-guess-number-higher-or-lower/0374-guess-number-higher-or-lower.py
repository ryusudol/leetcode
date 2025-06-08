# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        target = highest = n
        lowest = 1
        while guess(target) != 0:
            if guess(target) == -1:
                highest = target
                target = (target + lowest) // 2
            else:
                lowest = target
                target = (target + highest) // 2
        return target