# Time Complexity: O(n)
# Space Complexity: O(n)

class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        n = len(nums)
        earliest_occurence = {}
        earliest_occurence[0] = -1
        
        longest, run_sum = 0, 0
        for i, num in enumerate(nums):
            run_sum += -1 if not num else 1
            if run_sum not in earliest_occurence:
                earliest_occurence[run_sum] = i
            else:
                longest = max(longest, i - earliest_occurence[run_sum])

        return longest
