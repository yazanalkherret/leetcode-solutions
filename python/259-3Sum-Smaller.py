# Two Pointers
# Time Complexity: O(n^2)
# Space Complexity: O(1)

class Solution:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        triplets = 0
        for i in range(n - 2):
            triplets += self.two_sum_smaller(nums, target - nums[i], i + 1)

        return triplets

    def two_sum_smaller(self, nums, target, left):
        right = len(nums) - 1
        pairs = 0
        while left < right:
            two_sum = nums[left] + nums[right]
            if two_sum >= target:
                right -= 1
            else:
                pairs += right - left
                left += 1

        return pairs
