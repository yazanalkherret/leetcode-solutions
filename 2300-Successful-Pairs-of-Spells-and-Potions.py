# Time Complexity: O(n logn) -> Sorting
# Space Complexity: O(n) -> Sorting

class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        n, m = len(spells), len(potions)
        potions.sort()
        ans = []
        for num in spells:
            target = ceil(success / num)
            ndx = bisect_left(potions, target)
            ans.append(m - ndx)

        return ans