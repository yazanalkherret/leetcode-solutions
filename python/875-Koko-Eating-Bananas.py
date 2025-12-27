# Time Complexity: O(nlogm)
# Space Complexity: O(1)

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def canEatInK(k):
            return sum(ceil(val / k) for val in piles) <= h

        l, r = 1, max(piles)
        res = r
        while l <= r:
            m = (l + r) // 2
            if canEatInK(m):
                res = m
                r = m - 1
            else:
                l = m + 1
        return res 
