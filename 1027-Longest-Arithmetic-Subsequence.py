# Time Complexity: O(n^2)
# Space Complexity(n^2)

class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        N = len(nums)
        dp = [defaultdict(int) for _ in range(N)]
        res = 0
        for i in range(N - 1, -1, -1):
            for j in range(N -1, i, -1):
                diff = nums[j] - nums[i]
                dp[i][diff] = dp[j][diff] + 1
                res = max(res, dp[i][diff])

        return res + 1