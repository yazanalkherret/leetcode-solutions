# Time Complexity: O(number of bits)
# Space Complexity: O(1)

class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        diff = start ^ goal

        # Number of set bits - Brian Kernighan's algorithm
        res = 0
        while diff:
            diff = diff & (diff - 1)
            res += 1
        return res 

# One-liner
# Time Complexity: O(number of bits)
# Space Complexity: O(1)

class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        return (start ^ goal).bit_count()