# Time Complexity: O(n)
# Space Complexity: O(k)

class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        prefix = {0: -1}
        cur_prefix = 0
        for i, num in enumerate(nums):
            cur_prefix = (cur_prefix + num) % k

            if cur_prefix in prefix and prefix[cur_prefix] < i - 1:
                return True

            if cur_prefix not in prefix:
                prefix[cur_prefix] = i
            
        return False
