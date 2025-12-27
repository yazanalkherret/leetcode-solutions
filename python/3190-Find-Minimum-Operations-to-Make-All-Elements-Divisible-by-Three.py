# Time Complexity: O(n)
# Space Complexity: O(1)

class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        min_opereations = 0
        for num in nums:
            if num % 3:
                min_opereations += 1

        return min_opereations

# One-liner

class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        return sum(1 if num % 3 else 0 for num in nums)
