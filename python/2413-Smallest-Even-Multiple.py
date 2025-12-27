# Time Complexity: O(1)
# Space Complexity: O(1)

class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        return n << (n & 1)