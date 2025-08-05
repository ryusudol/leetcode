class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        memo = defaultdict(list)
        for s in strs:
            sorted_str = ''.join(sorted(s))
            memo[sorted_str].append(s)
        return list(memo.values())