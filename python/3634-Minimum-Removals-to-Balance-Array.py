# Sliding Window
# Time Complexity: O(n)
# Space Complexity: O(1)

class Solution:
    def minRemoval(self, nums: List[int], k: int) -> int:
        minRem = float("inf")
        n = len(nums)
        nums.sort()
        
        l, r = 0, 0
        while l < n:
            while r < n and nums[r] <= k * nums[l]:
                minRem = min(minRem, n - (r - l + 1))
                r += 1
            l += 1
        return minRem

# Dynamic Programming TLE/MLE
# Time Complexity: O(n^2)
# Space Complexity: O(n^2)

class Solution:
    def minRemoval(self, nums: List[int], k: int) -> int:
        n = len(nums)
        nums.sort()
        dp = [[float("inf")] * n for _ in range(n)]
        minRem = float("inf")
        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                if i == j:
                    dp[i][j] = n - 1

                elif nums[j]/k <= nums[i]:
                    dp[i][j] = dp[i][j - 1] - 1

                minRem = min(minRem, dp[i][j])
        return minRem