# Time Complexity: O(n logm)
# Space Complexity: O(1)

class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        def canFinishWithSpeed(x):
            time = 0
            for i in range(len(dist) - 1):
                time += ceil(dist[i] / x)

                if time > hour:
                    return False

            time += dist[-1] / x
            return time <= hour

        lo, hi = 1, max(dist) * 100
        res = -1

        while lo <= hi:
            mid = (lo + hi) // 2
            if canFinishWithSpeed(mid):
                res = mid
                hi = mid - 1
            else:
                lo = mid + 1
        
        return res
