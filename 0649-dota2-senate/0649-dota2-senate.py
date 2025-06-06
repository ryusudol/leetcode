class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        if len(senate) == 1:
            return 'Radiant' if senate[0] == 'R' else 'Dire'
        queue = list(senate)
        cur_r = cur_d = empty_count = 0
        while True:
            start_empty_count = empty_count
            for i in range(len(queue)):
                if queue[i] == 'R':
                    if cur_d > 0:
                        queue[i] = ''
                        empty_count += 1
                        cur_d -= 1
                        continue
                    cur_r += 1
                elif queue[i] == 'D':
                    if cur_r > 0:
                        queue[i] = ''
                        empty_count += 1
                        cur_r -= 1
                        continue
                    cur_d += 1
            end_empty_count = empty_count
            if start_empty_count == end_empty_count:
                break
        survived = ''
        for el in queue:
            if el == 'R' or el == 'D':
                survived = el
                break
        return 'Radiant' if survived == 'R' else 'Dire'