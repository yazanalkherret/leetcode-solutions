# Dynamic Programming
# Time Complexity: O(n)
# Space Complexity: O(1)

class Solution:
    def tribonacci(self, n: int) -> int:
        base = (0, 1, 1)
        if n <= 2: return base[n]

        prev3, prev2, prev1 = base

        for i in range(3, n + 1):
            temp = prev1 + prev2 + prev3
            prev3 = prev2
            prev2 = prev1
            prev1 = temp
        return prev1

# Time Complexity: O(n)
# Space Complexity: O(n)

class Solution:
    def tribonacci(self, n: int) -> int:
        dp = [0, 1, 1]
        if n <= 2: return dp[n]

        for i in range(3, n + 1):
            dp.append(dp[i - 1] + dp[i - 2] + dp[i - 3])
        return dp[n]