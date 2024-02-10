class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0
        str_len = len(s)
        if str_len == 0 or str_len == 1:
            return str_len
        for head in range(str_len):
            for tail in range(head, str_len):
                if s[head] == s[tail]:
                    unmatched = False
                    curr_head = head
                    curr_tail = tail
                    while curr_head < curr_tail:
                        if s[curr_head] != s[curr_tail]:
                            unmatched = True
                            break
                        curr_head += 1
                        curr_tail -= 1
                    if unmatched:
                        continue
                    count += 1
                    # print(s[head:tail+1])
        return count