class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        answer = [0] * len(temperatures)
        stack = []
        for idx, t in enumerate(temperatures):
            while stack and stack[-1][1] < t:
                date, _ = stack.pop()
                answer[date] = idx - date
            stack.append((idx, t))
        return answer