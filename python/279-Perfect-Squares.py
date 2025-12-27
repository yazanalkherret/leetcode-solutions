# Time Complexity: O(n * n^1/2)
# Space Complexity: O(n)

class Solution:
    def numSquares(self, n: int) -> int:
        
        cache = [n] * (n + 1)
        cache[0] = 0
        
        for i in range(1, n + 1):
            for s in range(1, i + 1):
                square = s * s
                if i - square < 0:
                    break
                cache[i] = min(cache[i], cache[i - square] + 1)

        return cache[n]