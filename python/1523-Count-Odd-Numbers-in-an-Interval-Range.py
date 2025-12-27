# Time Complexity: O(1)
# Space Complexity: O(1)

class Solution:
    def countOdds(self, low: int, high: int) -> int:
        length = high - low + 1
        return length // 2 + low % 2 if length % 2 else length // 2 