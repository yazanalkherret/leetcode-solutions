# Bruteforce
# Time Complexity: O(n^3)
# Space Complexity: O(1)

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        n = len(nums)
        res_sum, distance = float("inf"), float("inf")

        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    cur_sum = nums[i] + nums[j] + nums[k]
                    cur_distance = abs(cur_sum - target)

                    if cur_distance < distance:
                        res_sum = cur_sum
                        distance = cur_distance


        return res_sum
