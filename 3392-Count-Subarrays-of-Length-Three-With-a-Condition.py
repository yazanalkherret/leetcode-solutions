# Time Complexity: O(n)
# Space Complexity: O(1)

class Solution:
    def countSubarrays(self, nums: List[int]) -> int:
        n = len(nums)
        count = 0
        for i in range(2, n):
            if nums[i - 1] == (nums[i] + nums[i - 2]) * 2:
                count += 1
        return count