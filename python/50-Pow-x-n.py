# Iterative
# Time Complexity: O(logn)
# Space Complexity: O(1)

class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            x = 1 / x
            n = -n

        res = 1
        while n > 0:
            if n % 2 == 1:
                res *= x
            x *= x
            n //= 2

        return res


# Recursive
# Time Complexity: O(logn)
# Space Complexity: O(logn)

class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0: return 1
        if n < 0: return self.myPow(1/x, -n)

        half = self.myPow(x, n // 2)
        res = half * half

        return res * x if n % 2 else res

