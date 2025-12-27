# Bottom-up DP
# Time Complexity: O(m * n)
# Space Complexity: O(m * n)

class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        m, n = len(nums1), len(nums2)
        dp = [[0] * (n + 1) for _ in range(m + 1)] 

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if nums1[i - 1] != nums2[j - 1]: continue

                dp[i][j] = dp[i - 1][j - 1] + 1

        return max(dp[i][j] for j in range(n + 1) for i in range(m + 1))

# Top-down DP (MLE)
# Time Complexity: O(m * n)
# Space Complexity: O(m * n)

class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        @lru_cache(None)
        def dp(i, j):
            if i < 0 or j < 0:
                return 0

            if nums1[i] != nums2[j]:
                return 0

            return dp(i - 1, j - 1) + 1

        res = 0
        for i in range(len(nums1) - 1, -1, -1):
            for j in range(len(nums2) - 1, -1, -1):
                res = max(res, dp(i, j))

        return res
