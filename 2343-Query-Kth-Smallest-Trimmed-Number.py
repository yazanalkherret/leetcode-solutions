# Time Complexity: O(m*(n*trim+klogn))
# Space Complexity: O(m + n)

class Solution:
    def smallestTrimmedNumbers(self, nums: List[str], queries: List[List[int]]) -> List[int]:
        ans = []
        for i, (k, trim) in enumerate(queries):
            minheap = [(int(num[-trim:]), j) for j, num in enumerate(nums)]
            heapify(minheap)

            for _ in range(k - 1):
                heappop(minheap)

            ans.append(heappop(minheap)[1])
        return ans
