# String Int conversion
# Time Complexity: O(log10 n)
# Space Complexity: O(1)

class Solution:
    def reverse(self, x: int) -> int:
        isNegative = x < 0
        if isNegative: x *= -1

        res = int(str(x)[::-1])

        if isNegative: res *= - 1

        return res if res in range(-2 ** 31, 2 ** 31) else 0

# Math solution
# Time Complexity: O(log10 n)
# Space Complexity: O(1)

class Solution:
    def reverse(self, x: int) -> int:
        sign = -1 if x < 0 else 1
        res, x = 0, x * sign
        while x:
            x, rem = divmod(x, 10)
            res = res * 10 + rem
            if res > 2 ** 31 - 1:
                return 0
        return res * sign