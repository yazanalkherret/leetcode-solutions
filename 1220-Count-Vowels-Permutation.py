# Bottom-up DP
# Time Complexity: O(n)
# Space Complexity: O(1)

class Solution:
    def countVowelPermutation(self, n: int) -> int:
        MOD = 10 ** 9 + 7
        prev = [[1, 2, 4],
                [0, 2],
                [1, 3],
                [2],
                [2, 3]]

        prev_itr = [1] * 5

        for i in range(1, n):
            curr = [0] * 5
            for j in range(5):
                for jp in prev[j]:
                    curr[j] = (curr[j] + prev_itr[jp]) % MOD
            prev_itr = curr

        return sum(prev_itr) % MOD

# Bottom-up DP
# Time Complexity: O(n)
# Space Complexity: O(n)

class Solution:
    def countVowelPermutation(self, n: int) -> int:
        MOD = 10 ** 9 + 7
        prev = [[1, 2, 4],
                [0, 2],
                [1, 3],
                [2],
                [2, 3]]

        dp = [[0] * 5 for _ in range(n)]
        dp[0] = [1] * 5

        for i in range(1, n):
            for j in range(5):
                for jp in prev[j]:
                    dp[i][j] = (dp[i][j] + dp[i - 1][jp]) % MOD

        return sum(dp[-1]) % MOD

# Top-down DP
# Time Complexity: O(n)
# Space Complexity: O(n)

class Solution:
    def countVowelPermutation(self, n: int) -> int:
        MOD = 10 ** 9 + 7
        prev = [[1, 2, 4],
                [0, 2],
                [1, 3],
                [2],
                [2, 3]]

        @lru_cache(None)
        def dp(i, j):
            if i == 0: return 1

            ways = 0
            for jp in prev[j]:
                ways = (ways + dp(i - 1, jp)) % MOD
            
            return ways
        
        total_ways = 0

        for j in range(5):
            total_ways = (total_ways + dp(n - 1, j)) % MOD

        return total_ways
