# Time Complexity: O(n)
# Space Complexity: O(n)

class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        rearranged = [0] * len(nums)
        lastPositive, lastNegative = 0, 1
        for num in nums:
            if num >= 0:
                rearranged[lastPositive] = num
                lastPositive += 2
            else:
                rearranged[lastNegative] = num
                lastNegative += 2

        return rearranged
