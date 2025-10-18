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

# Time Complexity: O(maxTrim * n log n)
# Space Complexity: O(maxTrim * n)

class Solution:
    def smallestTrimmedNumbers(self, nums: List[str], queries: List[List[int]]) -> List[int]:
        maxTrim = max([t for _, t in queries])

        trimmedSorted = []

        # Construct table
        for i in range(1, maxTrim + 1):
            trimmed = []
            for j, num in enumerate(nums):
                trimmed.append((num[-i:], j))
            trimmedSorted.append(sorted(trimmed))
            
        ans = []
        for k, trim in queries:
            ans.append(trimmedSorted[trim - 1][k - 1][1])

        return ans