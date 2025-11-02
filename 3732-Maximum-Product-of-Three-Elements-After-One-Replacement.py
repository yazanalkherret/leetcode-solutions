# Time Complexity: O(nlogn)
# Space Complexity: O(n)

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        absnums = sorted([abs(num) for num in nums])
        return absnums[-1] * absnums[-2] * 100000