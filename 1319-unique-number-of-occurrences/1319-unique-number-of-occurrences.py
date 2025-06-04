class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        counter_values = Counter(arr).values()
        return len(set(counter_values)) == len(list(counter_values))