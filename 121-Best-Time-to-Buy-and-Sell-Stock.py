# Time complexity: O(n)
# Space Complexity: O(1)

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        maxSell, maxProfit = 0, 0

        for i in range(n - 1, -1, -1):
            maxSell = max(maxSell, prices[i])
            maxProfit = max(maxProfit, maxSell - prices[i])

        return maxProfit