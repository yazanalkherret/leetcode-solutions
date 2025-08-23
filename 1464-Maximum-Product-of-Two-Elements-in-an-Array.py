# Time: O(n log n) for sorting
# Space: O(n) for sorting

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        nums.sort() 
        first, second = nums[-1] - 1, nums[-2] - 1
        return first * second