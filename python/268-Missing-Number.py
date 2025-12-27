# Sum Formula
# Time Complexity: O(n)
# Space Complexity: O(1)

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        total = n * (n + 1) // 2
        return total - sum(nums)
    
# Bit Manipulation
# Time Complexity: O(n)
# Space Complexity: O(1)

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        res = len(nums)
        for i in range(len(nums)):
            res ^= i ^ nums[i]

        return res