# Time Complexity: O(n + k log n)
# Space Complexity: O(n)

class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        maxHeap = [int(num) * - 1 for num in nums] # Negative int val of every num
        heapq.heapify(maxHeap)

        res = None
        for _ in range(k):
            res = heapq.heappop(maxHeap) # Return value will be negative

        return str(res * -1)