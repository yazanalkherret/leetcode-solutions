# Time Complexity: O(n)
# Space Complexity: O(n)

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        runSum = nums[::]
        for i in range(1, len(nums)):
            runSum[i] += runSum[i - 1]
        return runSum