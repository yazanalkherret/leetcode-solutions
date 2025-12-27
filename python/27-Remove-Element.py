class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        countTarget = 0

        for ndx, num in enumerate(nums):
            if num == val:
                nums[ndx] = float('inf')
                countTarget += 1

        k = len(nums) - countTarget

        l, r = 0, len(nums) - 1
        while l < r:
            if nums[l] == float('inf'):
                while l < r and nums[r] == float('inf'):
                    r -= 1
                nums[l], nums[r] = nums[r], nums[l]
            l += 1

        return k

# Simpler Solution
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
        
        return k