class Solution:
    def reverse(self, x: int) -> int:
        x = list(str(x))
        x.reverse()
        if x[-1] == '-':
            x.pop()
            x.insert(0, '-')
        elif x[0] == '0':
            if len(x) == 1:
                return 0
            while x[0] == '0':
                x.pop(0)
        ans = ''.join(el for el in x)
        if int(ans) < pow(2, 31) * -1 or int(ans) > pow(2, 31) - 1:
            return 0
        return int(ans)