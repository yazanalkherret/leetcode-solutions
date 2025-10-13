# Time Complexity: O(n)
# Space Complexity: O(n)

class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [-1] * n

        stack = []        
        for i in range(2 * n):
            i %= n
            while stack and nums[i] > stack[-1][0]:
                small, smallNdx = stack.pop()
                ans[smallNdx] = nums[i]
            stack.append((nums[i], i))

        return ans