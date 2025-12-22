# Time Complexity: ~O(nlogn)
# Space Complexity: O(1)

class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:

        def waviness(num):
            res = 0
            prev, prev2 = num // 10 % 10, num % 10
            num //= 100

            while num > 0:
                curr = num % 10
                if prev > curr and prev > prev2 or prev < curr and prev < prev2:
                    res += 1
                prev, prev2 = curr, prev
                num //= 10

            return res
    
        return sum(waviness(num) for num in range(num1, num2 + 1))
