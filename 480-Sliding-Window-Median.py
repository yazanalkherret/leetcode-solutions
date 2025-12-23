# Time Complexity: O(nlogk)
# Space Complexity: O(k)

class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        n = len(nums)
        res = []

        # Initial window
        sl = sortedcontainers.SortedList(nums[:k])
        res.append(self.median(sl))

        for r in range(k, n):
            sl.remove(nums[r - k])
            sl.add(nums[r])
            res.append(self.median(sl))

        return res

    def median(self, sl):
        if len(sl) % 2:
            return sl[len(sl) // 2]
        else:
            return (sl[len(sl) // 2] + sl[len(sl) // 2 - 1]) / 2
