# One-liner
class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        return n

# Added Algo to calculate GCD for general cases

class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        # Math
        sumEven = n * (n + 1)
        sumOdd = n * n

        # Euclid
        while sumOdd != 0:
            temp = sumOdd
            sumOdd = sumEven % sumOdd
            sumEven = temp

        return sumEven