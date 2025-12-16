# Time Complexity: O(logn)
# Space Complexity: O(1)

class Solution:
    def firstBadVersion(self, n: int) -> int:
        l, r = 1, n
        while l <= r:
            m = (l + r) // 2
            if isBadVersion(m):
                r = m - 1
            else:
                l = m + 1
        return l
