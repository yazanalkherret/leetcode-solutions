# Time Complexity: O(n)
# Space Complexity: O(1)

class Solution:
    def evenNumberBitwiseORs(self, nums: List[int]) -> int:
        res = 0
        for num in nums:
            if not (num & 1):
                res |= num
        return res