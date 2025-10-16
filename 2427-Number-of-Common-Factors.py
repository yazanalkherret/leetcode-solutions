# Time Complexity: O(gcd(a,b))
# Space Complexity: O(1)

class Solution:
    def commonFactors(self, a: int, b: int) -> int:
        count = 0
        for i in range(1, gcd(a, b) + 1):
            if a % i == b % i == 0:
                count += 1

        return count
        