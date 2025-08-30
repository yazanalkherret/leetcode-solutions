# Dynamic Programming
# Time Complexity: O(n)
# Space Complexity: O(1)

class Solution:
    def fib(self, n: int) -> int:
        prev, prev2 = 0, 0

        for i in range(n + 1):
            if i < 2: F = i
            else: F = prev + prev2
            prev2, prev = prev, F

        return prev