# Time Complexity: O(n * log(m * max_rank))
# Space Complexity: O(1)

class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        
        def canRepairIn(minutes):
            num_repaired = 0
            for rank in ranks:
                num_repaired += floor(sqrt(minutes // rank))

            return num_repaired >= cars

        lo, hi = 1, max(ranks) * cars * cars
        res = hi
        while lo <= hi:
            mid = (lo + hi) // 2
            if canRepairIn(mid):
                res = mid
                hi = mid - 1
            else:
                lo = mid + 1

        return res

