# Time Complexity: O(n)
# Space Complexity: O(1)

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        n = len(nums)       
        l = 0
        count_zeroes = 0
        max_res = 0

        for r in range(n):
            if not nums[r]:
                count_zeroes += 1

            while l < n and count_zeroes > k:
                if not nums[l]:
                    count_zeroes -= 1
                l += 1

            max_res = max(max_res, r - l + 1)
            
        return max_res
