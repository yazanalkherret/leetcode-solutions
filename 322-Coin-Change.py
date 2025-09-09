# Time Complexity: O(amount* len(coins))
# Space Complexity: O(amount)

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = [float("inf")] * (amount + 1)
        memo[0] = 0

        for i in range(1, amount + 1):
            for coin in coins:
                if i - coin >= 0:
                    memo[i] = min(memo[i], memo[i - coin] + 1)

        return memo[amount] if memo[amount] != float("inf") else -1