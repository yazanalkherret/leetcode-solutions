# Time Complexity: O(n)
# Space Complexity: O(n)

class Solution:
    def numberOfSubarrays(self, nums: List[int]) -> int:
        ans = 0
        stack = []

        for curr in nums:
            while stack and curr > stack[-1][0]:
                ans += 1
                stack.pop()
            if stack and curr == stack[-1][0]:
                ans += stack[-1][1]
                stack.append([curr, stack[-1][1] + 1])
            else:
                stack.append([curr, 1])

        return ans + len(stack)