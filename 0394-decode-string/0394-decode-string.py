class Solution:
    def decodeString(self, s: str) -> str:
        # Better Solution -> Key: storing the # of interation and a substr together
        stack = []
        cur_num = 0
        cur_str = ""
        for ch in s:
            if ch.isdigit():
                cur_num = cur_num * 10 + int(ch)
            elif ch == "[":
                stack.append((cur_str, cur_num))
                cur_str = ""
                cur_num = 0
            elif ch == "]":
                prev_str, num = stack.pop()
                cur_str = prev_str + cur_str * num
            else:
                cur_str += ch

        return cur_str

        # My First Solution -> Complicated
        # num_stack = []
        # substr_stack = []
        # ans = num = substr = ''
        # open_count = 0
        # for c in s:
        #     if '0' <= c <= '9':
        #         num += c
        #     elif c == '[':
        #         num_stack.append((int(num), bool(substr)))
        #         num = ''
        #         open_count += 1
        #         if substr:
        #             substr_stack.append(substr)
        #             substr = ''
        #     elif c == ']':
        #         open_count -= 1
        #         iter_count, substr_stack_pop = num_stack.pop()
        #         if open_count == 0:
        #             for _ in range(iter_count):
        #                 ans += substr
        #             substr = ''
        #         else:
        #             temp = ''
        #             for _ in range(iter_count):
        #                 temp += substr
        #             substr = substr_stack.pop() + temp if substr_stack_pop else temp
        #     elif open_count == 0:
        #         ans += c
        #     else:
        #         substr += c
        #     print(substr, num_stack, substr_stack)
        # return ans