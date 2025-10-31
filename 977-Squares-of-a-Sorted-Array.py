# Time Complexity: O(n)
# Space Complexity: O(n)

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [0] * n

        l, r = 0, n - 1
        curr = n - 1
        while l <= r:
            if nums[l] ** 2 >= nums[r] ** 2:
                ans[curr] = nums[l] ** 2
                l += 1
            else:
                ans[curr] = nums[r] ** 2
                r -= 1

            curr -= 1

        return ans
