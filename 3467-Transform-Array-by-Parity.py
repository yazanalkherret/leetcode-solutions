# Time Complexity: O(n)
# Space Complexity: O(n)

class Solution:
    def transformArray(self, nums: List[int]) -> List[int]:
        numOdd, numEven = 0, 0
        n = len(nums)
        for num in nums:
            numOdd += num & 1
        numEven = n - numOdd
        
        return [0] * numEven + [1] * numOdd