# Time Complexity: O(n + k log n)
# Space Complexity: O(n)

import heapq
class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        pq = []
        for i, num in enumerate(nums):
            pq.append([num, i])

        heapify(pq) # compared lexicographically

        for _ in range(k):
            curr = heappop(pq)
            curr[0] *= multiplier
            heappush(pq, curr)

        res = [-1] * len(nums)
        for val, ndx in pq:
            res[ndx] = val
        return res