# Bottom-up
# Time Complexity: O(t * n)
# Space Complexity: O(t)
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = [0] * (target + 1)
        dp[0] = 1

        for i in range(1, target + 1):
            for num in nums:
                if i - num >= 0:
                    dp[i] += dp[i - num]

        return dp[-1]

# Top-down
# Time Complexity: O(t * n)
# Space Complexity: O(t)

class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        @lru_cache(None)
        def helper(amount):
            if amount == 0: return 1
            if amount < 0: return 0

            ways = 0
            for num in nums:
                ways += helper(amount - num)
            return ways

        return helper(target)
