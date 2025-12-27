# Time Complexity: O(nlogm)
# Space Complexity: O(1)

class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def possible(cap):
            days_used = 1
            cur = 0
            for w in weights:
                if cur + w <= cap:
                    cur += w
                else:
                    days_used += 1
                    cur = w
                    if days_used > days:
                        return False
            return True

        l, r = max(weights), sum(weights)
        res = r
        while l <= r:
            m = (l + r) // 2
            if possible(m):
                res = m
                r = m - 1
            else:
                l = m + 1
        return res
