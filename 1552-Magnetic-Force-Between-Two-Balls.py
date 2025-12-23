# Optimal
# Time Complexity: O(n logd)
# Space Complexity: O(n) -> Sorting

class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        def doable(x):
            last_pos = position[0]
            count = 1
            for i in range(1, len(position)):
                if position[i] - last_pos >= x:
                    count += 1
                    last_pos = position[i]
                
                if count == m:
                    return True

            return False

        position.sort()

        lo, hi = 1, position[-1] // (m - 1)
        res = 0
        while lo <= hi:
            mid = (lo + hi) // 2
            if doable(mid):
                res = mid
                lo = mid + 1
            else:
                hi = mid - 1

        return res


# Time Complexity: O(nlogn + m logn logd)
# Space Complexity: O(n) -> Sorting

class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        def doable(x, start_index = 0):
            for _ in range(m - 1):
                curr_bucket = position[start_index]
                next_index = bisect_left(position, curr_bucket + x)

                if next_index == len(position): 
                    return False

                start_index = next_index

            return True

        position.sort()

        lo, hi = 0, position[-1] - position[0]
        res = 0
        while lo <= hi:
            mid = (lo + hi) // 2
            if doable(mid):
                res = mid
                lo = mid + 1
            else:
                hi = mid - 1

        return res
