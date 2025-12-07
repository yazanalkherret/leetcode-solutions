# Time Complexity: O(log(d[0] + d[1]))
# Space Complexity: O(1)

class Solution:
    def minimumTime(self, d: List[int], r: List[int]) -> int:
        def canInTime(time):
            free1 = time - time // r[0]
            free2 = time - time // r[1]
            total = time - time // lcm(r[0], r[1])
            return free1 >= d[0] and free2 >= d[1] and total >= d[0] + d[1]

        left, right = d[0] + d[1], 2 * (d[0] + d[1])
        res = right
        while left <= right:
            m = (left + right) // 2
            if canInTime(m):
                res = m
                right = m - 1
            else:
                left = m + 1
        return res
