# Time Complexity: O(n log n)
# Space Complexity: O(n)

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-x for x in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            first = heapq.heappop(stones) * -1
            second = heapq.heappop(stones) * -1
            diff = abs(first - second)
            if diff: heapq.heappush(stones, diff * -1)
            
        return stones[0] * -1 if stones else 0