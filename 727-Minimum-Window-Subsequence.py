# Bottom-up Dynamic Programming
# Time Complexity: O(m * n)
# Space Complexity: O(m * n)
# It is possible to improve the space complexity to O(m) or O(n)

class Solution:
    def minWindow(self, s1: str, s2: str) -> str:
        m, n = len(s1), len(s2)
        
        min_window = float("inf")
        substr_res = ""

        dp = [[float("inf")] * (n + 1) for _ in range(m + 1)]

        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if j == n - 1 and s1[i] == s2[j]:
                    dp[i][j] = i
                elif s1[i] == s2[j]:
                    dp[i][j] = dp[i + 1][j + 1]
                else:
                    dp[i][j] = dp[i + 1][j]
        
        for i in range(m):
            if dp[i][0] - i + 1 < min_window:
                min_window = dp[i][0] - i + 1
                substr_res = s1[i:dp[i][0] + 1]

        return substr_res

# Top-down Dynamic Programming
# Time Complexity: O(m * n)
# Space Complexity: O(m * n)

class Solution:
    def minWindow(self, s1: str, s2: str) -> str:
        m, n = len(s1), len(s2)
        
        @lru_cache(None)
        def dp(i, j):
            if j == n or i == m:
                return float("inf")

            if j == n - 1 and s1[i] == s2[j]:
                return i
            
            if s1[i] == s2[j]:
                return dp(i + 1, j + 1)

            return dp(i + 1, j)
        
        min_window = float("inf")
        substr_res = ""
        
        for i in range(m):
            if dp(i, 0) - i + 1 < min_window:
                min_window = dp(i, 0) - i + 1
                substr_res = s1[i:dp(i, 0) + 1]

        return substr_res


# Hashmaps
# Time Complexity: Avg O(m * n), Worst O(m^2 * n)?
# Space Complexity: O(m + n)

class Solution:
    def minWindow(self, s1: str, s2: str) -> str:
        m, n = len(s1), len(s2)
        closest_index = {}

        hashmaps = [None] * m

        for i in range(m - 1, -1, -1):
            hashmaps[i] = closest_index.copy()
            closest_index[s1[i]] = i

        @lru_cache(None)
        def subseq_end(original_index, subseq_index):
            if subseq_index == n - 1:
                return original_index

            if s2[subseq_index + 1] not in hashmaps[original_index]:
                return float("inf")

            return subseq_end(hashmaps[original_index][s2[subseq_index + 1]], subseq_index + 1)

        min_window_len = float("inf")
        substr = ""
        for i, char in enumerate(s1):
            if char == s2[0]:
                window_end = subseq_end(i, 0)
                window_len = window_end - i + 1
                if window_len < min_window_len:
                    min_window_len = window_len
                    substr = s1[i:window_end + 1]

        return substr
