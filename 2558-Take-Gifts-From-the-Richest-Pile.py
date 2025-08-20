# Time complexity: O(n + k log n)
# Space Complexity: O(n)

import heapq
class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        gifts = [-g for g in gifts] 
        heapify(gifts)

        for _ in range(k):
            curr = heappop(gifts) * -1 
            curr = floor(sqrt(curr))
            heappush(gifts, curr * -1)

        return sum(gifts) * -1