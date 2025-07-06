class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        n, m = len(spells), len(potions)
        potions.sort()
        pairs = []
        for spell in spells:
            min_required_potion = success // spell + (1 if success % spell else 0)
            i = bisect.bisect_left(potions, min_required_potion)
            pairs.append(len(potions) - i)
        return pairs