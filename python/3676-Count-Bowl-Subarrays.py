# Time Complexity: O(n)
# Space Complexity: O(n)

class Solution:
    def bowlSubarrays(self, nums: List[int]) -> int:
        stack = []
        res = 0

        for i, num in enumerate(nums):
            while stack and num >= stack[-1][0]:
                popval, popndx = stack.pop()
                if i - popndx >= 2:
                    res += 1
            
            if stack and i - stack[-1][1] >= 2:
                res += 1
                
            stack.append((num, i))

        return res
