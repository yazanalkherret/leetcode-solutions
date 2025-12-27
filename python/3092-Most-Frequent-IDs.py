# Time Complexity: O(nlogn)
# Space Complexity: O(n)

class Solution:
    def mostFrequentIDs(self, nums: List[int], freq: List[int]) -> List[int]:
        updatedFreq = defaultdict(int)
        heap = []
        ans = []
        for n, f in zip(nums, freq):
            updatedFreq[n] += f
            heappush(heap, (-updatedFreq[n], n))

            while -heap[0][0] != updatedFreq[heap[0][1]]:
                heappop(heap)

            ans.append(-heap[0][0])

        return ans