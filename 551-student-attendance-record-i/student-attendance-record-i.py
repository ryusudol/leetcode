class Solution:
    def checkRecord(self, s: str) -> bool:
        count_A, count_L = 0, 0
        for c in s:
            if c == 'P':
                count_L = 0
            elif c == 'A':
                count_L = 0
                count_A += 1
                if count_A > 1:
                    return False
            elif c == 'L':
                count_L += 1
                if count_L == 3:
                    return False
        return True