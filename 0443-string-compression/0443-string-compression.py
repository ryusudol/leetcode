class Solution:
    def compress(self, chars: List[str]) -> int:
        if len(chars) == 1:
            return 1
        s, prev_c = '', chars[0]
        count = 1
        for idx, c in enumerate(chars[1:], start=1):
            if prev_c != c:
                s += prev_c + (str(count) if count != 1 else '') + (c if idx == len(chars) - 1 else '')
                prev_c = c
                count = 1
            else:
                count += 1
                if idx == len(chars) - 1:
                    s += c + (str(count) if count != 1 else '')
        chars[:len(s)] = s
        return len(s)