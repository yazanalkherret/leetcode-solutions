# Time Complexity: O(sqrt(n))
# Space Complexity: O(1)

class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        numEmpty, drunk = 0, 0
        while numBottles > 0:
            drunk += numBottles
            numEmpty += numBottles
            numBottles = 0

            if numEmpty >= numExchange:
                numEmpty -= numExchange
                numBottles += 1
                numExchange += 1

        return drunk
            
# Short

class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        ans = numBottles
        empty = numBottles
        while empty >= numExchange:
            ans += 1
            empty -= numExchange - 1
            numExchange += 1
        return ans