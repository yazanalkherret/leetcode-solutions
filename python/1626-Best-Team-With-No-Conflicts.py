# Bottom-up DP
# Time Complexity: O(n^2)
# Space Complexity: O(n)

class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        n = len(scores)
        merged = sorted([(age, score) for age, score in zip(ages, scores)])
        dp = [score for _, score in merged]
        res = dp[0]

        for i in range(n):
            age_i, score_i = merged[i]
            for j in range(i):
                age_j, score_j = merged[j]
                if age_i == age_j or score_i >= score_j:
                    dp[i] = max(dp[i], score_i + dp[j])
            res = max(res, dp[i])

        return res

# Top-down DP
# Time Complexity: O(n^2)
# Space Complexity: O(n)

class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        n = len(scores)
        merged = sorted([(age, score) for age, score in zip(ages, scores)])

        @lru_cache(None)
        def dp(i):
            if i == 0: return merged[0][1]

            age_i ,score_i = merged[i]
            best_score = score_i
            for j in range(i):
                age_j, score_j = merged[j]
                if age_i == age_j or score_i >= score_j:
                    best_score = max(best_score, score_i + dp(j))
            return best_score

        
        max_score = merged[0][1]
        for i in range(n - 1, -1, -1):
            max_score = max(max_score, dp(i))
        return max_score
