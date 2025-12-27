# Patience Sort

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        patsort = []
        
        for i in nums:
            if not patsort or i > patsort[-1]:
                patsort.append(i)
            else:
                patsort[bisect.bisect_left(patsort, i)] = i
            
        return len(patsort)

# Dynamic Programming
# Time Complexity: O(n^2)
# Space Complexity: O(n)

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        N = len(nums)
        memo = [1] * N
        res = 1

        for i in range(N - 1, -1, -1):
            for j in range(i, N):
                if nums[i] < nums[j]:
                    memo[i] = max(memo[i], 1 + memo[j])
            res = max(res, memo[i])

        return res

