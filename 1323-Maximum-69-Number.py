class Solution:
    def maximum69Number (self, num: int) -> int:
        # Starting from 4 because max constraint for num is 10*4 (num = 9999)
        # (num // 10 ** i) % 10 picks the digit at i
        # Time, Space: O(1)
        for i in range(4, -1, -1):
            if (num // 10 ** i) % 10 == 6:
                num += 3 * 10 ** i
                return num
        return num