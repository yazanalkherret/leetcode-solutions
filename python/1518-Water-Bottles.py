# Time Complexity: O(log n)
# Space Complexity: O(1)

class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        drink, empty = 0, 0
        while numBottles > 0:
            drink += numBottles
            empty += numBottles
            numBottles, empty = divmod(empty, numExchange)

        return drink 