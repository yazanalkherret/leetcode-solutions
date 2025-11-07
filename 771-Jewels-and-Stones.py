# Time Complexity: O(m + n)
# Space Complexity: O(m)

class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        ans = 0
        j = set(jewels)
        for c in stones:
            if c in j:
                ans += 1

        return ans