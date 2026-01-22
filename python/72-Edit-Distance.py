# Time Complexity: O(m * n)
# Space Complexity: O(m * n)

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        dp[0] = [i for i in range(n + 1)]
        
        for i in range(m + 1):
            dp[i][0] = i

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]

                else:
                    delete = dp[i - 1][j]
                    replace = dp[i - 1][j - 1]
                    insert = dp[i][j - 1]

                    dp[i][j] = min(delete, replace, insert) + 1

        return dp[m][n]

# Time Complexity: O(m * n)
# Space Complexity: O(m * n)

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        
        @lru_cache(None)
        def dp(ptr1, ptr2):

            if ptr1 == -1:
                return ptr2 + 1

            if ptr2 == -1:
                return ptr1 + 1
            
            if word1[ptr1] == word2[ptr2]:
                return dp(ptr1 - 1, ptr2 - 1)

            delete = dp(ptr1 - 1, ptr2)
            insert = dp(ptr1, ptr2 - 1)
            replace = dp(ptr1 - 1, ptr2 - 1)

            min_distance = min(delete, insert, replace) + 1
            return min_distance

        return dp(len(word1) - 1, len(word2) - 1)
        