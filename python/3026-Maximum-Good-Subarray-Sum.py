# Time Complexity: O(n)
# Space Complexity: O(n)

class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        prefix = [0] + nums[::]
        prevMin = defaultdict(lambda : float("inf"))
        ans = float("-inf")
        for i in range(1, n + 1):
            prefix[i] += prefix[i - 1]
            
        for i, num in enumerate(nums):
            prevMin[nums[i]] = min(prevMin[nums[i]], prefix[i])
            ans = max(ans, prefix[i + 1] - min(prevMin[num + k], prevMin[num - k]))

        return ans if ans != float("-inf") else 0