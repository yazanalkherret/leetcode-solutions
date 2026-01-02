# Binay Exponentiation
# Time Complexity: O(logn)
# Space Complexity: O(1)

class Solution:
    def countGoodNumbers(self, n: int) -> int:
        MOD = 10 ** 9 + 7
        def pow_mod(x, n, mod):
            res = 1
            while n > 0:
                if n & 1:
                    res = res * x % mod

                x = x * x % mod
                n //= 2
            return res

        return pow_mod(5, (n + 1) // 2, MOD) * pow_mod(4, n // 2, MOD) % MOD
