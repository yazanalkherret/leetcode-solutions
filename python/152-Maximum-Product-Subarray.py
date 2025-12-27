# Time Complexity: O(n)
# Space Complexity: O(n)

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [[1, 1] for _ in range(n + 1)]
        best = nums[0]

        for i in range(1, n + 1):
            first = nums[i - 1] * dp[i - 1][0]
            second = nums[i - 1] * dp[i - 1][1]
            best = max(best, first, second)

            dp[i][0] = max(first, second) if max(first, second) > 0 else 1
            dp[i][1] = min(first, second) if min(first, second) < 0 else 1
            

        return best
