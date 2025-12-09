# Time Complexity: O(nlogn)
# Space Complexity: O(n)

class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        freq = Counter(nums)
        unique = sorted(list(set(nums)))
        n = len(unique)
        dp = [0] * (n + 2)

        for i in range(2, n + 2):
            if unique[i - 3] == unique[i - 2] - 1:
                dp[i] = max(dp[i - 1], dp[i - 2] + unique[i - 2] * freq[unique[i - 2]])
            else:
                dp[i] = dp[i - 1] + unique[i - 2] * freq[unique[i - 2]]

        return dp[-1]
