class Solution:
    def totalMoney(self, n: int) -> int:
        completeSum = 28 * floor(n / 7) + 7 * ((floor(n / 7) - 1) * floor(n / 7)) / 2
        remainingSum = (n % 7) * floor(n / 7) + (n % 7 * (n % 7 + 1)) / 2
        return int(completeSum + remainingSum)

class Solution:
    def totalMoney(self, n: int) -> int:
        q = n // 7
        r = n % 7
        total = (7 * q * (q + 7) + r * (2 * q + r + 1)) // 2
        return total