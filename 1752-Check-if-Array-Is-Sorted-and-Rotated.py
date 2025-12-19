# Time Complexity: O(n)
# Space Complexity: O(1)

class Solution:
    def check(self, nums: List[int]) -> bool:
        n = len(nums)

        inversion_count = 0

        for index in range(1, n):
            if nums[index] < nums[index - 1]:
                inversion_count += 1
                if inversion_count > 1:
                    return False

        if nums[0] < nums[n - 1]:
            inversion_count += 1

        return inversion_count <= 1
