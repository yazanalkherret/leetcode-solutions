# Top-down Dynamic Programming
# Time Complexity: O()
# Space Complexity: O()

class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        cache = {}

        def fun(pathLength):
            if pathLength > high: return 0
            if pathLength in cache: return cache[pathLength]

            res = fun(pathLength + zero) + fun(pathLength + one) 
            
            if pathLength >= low:
                res += 1

            res %= 10 ** 9 + 7
            cache[pathLength] = res
            return res

        return fun(0)