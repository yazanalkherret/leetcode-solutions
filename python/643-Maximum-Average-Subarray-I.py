# Time Complexity: O(n)
# Space Complexity: O(1)

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        window_sum = sum(nums[:k])
        window_avg = window_sum / k

        left = 0
        for right in range(k, len(nums)):
            window_sum += nums[right] - nums[left]
            window_avg = max(window_avg, window_sum / k)
            left += 1

        return window_avg
