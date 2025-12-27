# Time Complexity: O(n)
# Space Complexity: O(n)

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count, total = 0, 0
        sumFreq = defaultdict(int)
        sumFreq[0] = 1

        for i in range(len(nums)):
            total += nums[i]
            count += sumFreq[total - k]

            sumFreq[total] += 1

        return count