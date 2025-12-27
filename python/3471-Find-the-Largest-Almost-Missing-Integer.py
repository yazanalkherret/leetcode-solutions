# Time Complexity: O(n * k)
# Space Complexity: O(n)

class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        n = len(nums)
        freq = defaultdict(int)
        l, r = 0, k - 1
        
        while l < n and r < n:
            for num in set(nums[l:r+1]):
                freq[num] += 1
            l += 1
            r += 1

        res = -1
        for k, v in freq.items():
            if v == 1:
                res = max(res, k)
        return res