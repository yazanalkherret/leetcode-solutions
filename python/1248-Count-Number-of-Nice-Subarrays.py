# Prefix sum
# Time Complexity: O(n)
# Space Complexity: O(n)

class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        subarrays = 0
        binary_nums = [num & 1 for num in nums]
        running_sum = 0
        seen_sums_freq = defaultdict(int)

        for num in binary_nums:
            running_sum += num
            if running_sum == k:
                subarrays += 1

            subarrays += seen_sums_freq[running_sum - k]
            seen_sums_freq[running_sum] += 1

        return subarrays

# Sliding Window 
# Time Complexity: O(n)
# Space Complexity: O(1)

class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        def subarrays_at_most_x_odd(x):
            left, subarrays = 0, 0
            count_odd = 0
            for right, num in enumerate(nums):
                count_odd += num % 2

                while count_odd > x:
                    if nums[left] % 2:
                        count_odd -= 1
                    left += 1

                window_size = right - left + 1
                subarrays += window_size

            return subarrays

        return subarrays_at_most_x_odd(k) - subarrays_at_most_x_odd(k - 1)