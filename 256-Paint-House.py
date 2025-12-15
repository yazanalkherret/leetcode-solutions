# Better DP
# Time Complexity: O(n)
# Space Complexity: O(1)

class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        n = len(costs)
        dp = costs[0][::]

        for i in range(1, n):
            curr = [0, 0, 0]
            for c in range(3):
                curr[c] = costs[i][c] + min(dp[(c + 1) % 3], dp[(c + 2) % 3])
            dp = curr
            
        return min(dp)

# Bottom-up Dynamic Programming
# Time Complexity: O(n)
# Space Complexity: O(n)

class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        n = len(costs)
        dp = [costs[0][::] for _ in range(n)]

        for i in range(1, n):
            for c in range(3):
                dp[i][c] = costs[i][c] + min(dp[i - 1][(c + 1) % 3], dp[i - 1][(c + 2) % 3])

        return min(dp[-1]) 

# Top-down Dynamic Programming
# Time Complexity: O(n)
# Space Complexity: O(n)

class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        n = len(costs)
        
        @lru_cache(None)
        def dp(i, c):
            if i == 0:
                return costs[i][c]

            return costs[i][c] + min(dp(i - 1, (c + 1) % 3), dp(i - 1, (c + 2) % 3))

        return min(dp(n - 1, 0), dp(n - 1, 1), dp(n - 1, 2))

