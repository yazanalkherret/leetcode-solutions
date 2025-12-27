# Time Complexity: O(n)
# Space Complexity: O(value)

class Solution:
    def findSmallestInteger(self, nums: List[int], value: int) -> int:
        n = len(nums)
        modResidues = [0] * value

        for num in nums:
            modResidues[num % value] += 1
        
        for i in range(n):
            if modResidues[i % value] == 0:
                return i
            
            modResidues[i % value] -= 1

        return n 