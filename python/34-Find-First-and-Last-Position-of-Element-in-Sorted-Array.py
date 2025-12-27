# Time Complexity: O(logn)
# Space Complexity: O(1)

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        return [self.searchLeft(nums, target), self.searchRight(nums, target)]

    def searchLeft(self, nums, target):
        l, r = 0, len(nums) - 1
        found = -1
        while l <= r:
            m = (l + r) // 2
            if nums[m] > target:
                r = m - 1
            elif nums[m] < target:
                l = m + 1
            else:
                found = m
                r = m - 1

        return found

    def searchRight(self, nums, target):
        l, r = 0, len(nums) - 1
        found = -1
        while l <= r:
            m = (l + r) // 2
            if nums[m] > target:
                r = m - 1
            elif nums[m] < target:
                l = m + 1
            else:
                found = m
                l = m + 1

        return found
