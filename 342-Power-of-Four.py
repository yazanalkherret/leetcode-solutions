class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n <= 0: return False
        x = math.log2(n) // 2
        return 4 ** x == n