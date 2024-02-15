class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if c == '(': stack.append(')')
            elif c == '[': stack.append(']')
            elif c == '{': stack.append('}')
            elif not stack: return False
            elif c == stack[-1]: stack.pop()
            else: return False
        if stack: return False
        return True