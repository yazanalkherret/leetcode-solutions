# Total Time Complexity: O(nlogn)
# Total Space complexity: O(n)

class Solution:
    def isActiveAtTime(self, time, s, order, k):
        n = len(s)
        stars = [False] * n
        for i in range(time + 1):
            stars[order[i]] = True
        
        totalSubstrs = n * (n + 1) // 2
        invalidSubstrs = 0
        
        start, end = 0, n
        for i in range(n):
            if not stars[i]: continue

            end = i
            invalidSubstrs += (end - start) * (end - start + 1) // 2
            start = end + 1

        invalidSubstrs += (n - start) * (n - start + 1) // 2

        validSubstrs = totalSubstrs - invalidSubstrs

        return validSubstrs >= k

    def minTime(self, s: str, order: List[int], k: int) -> int:
        n = len(s)
        l, r, res = 0, n - 1, -1

        while l <= r:
            m = (l + r) // 2
            if self.isActiveAtTime(m, s, order, k):
                res = m
                r = m - 1
            else:
                l = m + 1

        return res