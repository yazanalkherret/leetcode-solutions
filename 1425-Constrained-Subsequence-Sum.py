# Time Complexity: O(nlogn)
# Space Complexity: O(n)

class Solution:
    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        
        heap = [(-nums[0], 0)]
        best_res = nums[0]

        for j in range(1, n):
            while heap and heap[0][1] < j - k:
                heappop(heap)

            curr = nums[j] + max(0, -heap[0][0])
            best_res = max(best_res, curr)
            heappush(heap, (-curr, j))

        return best_res
