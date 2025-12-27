# Time Complexity: O(n)
# Space Complexity: O(n)

class Solution:
    def maxSum(self, nums: List[int]) -> int:
        unique = set()
        maxx = max(nums)
        for num in nums:
            if num >= 0:
                unique.add(num)
        return sum(unique) if unique else maxx
