# Time Complexity: O(n)
# Space Complexity: O(1)

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxOnes, currOnes = 0, 0
        for num in nums:
            if num:
                currOnes += 1
                maxOnes = max(maxOnes, currOnes)
            else:
                currOnes = 0
        return maxOnes
