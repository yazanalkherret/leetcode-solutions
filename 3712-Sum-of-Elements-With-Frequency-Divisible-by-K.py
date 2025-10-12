class Solution:
    def sumDivisibleByK(self, nums: List[int], k: int) -> int:
        count = Counter(nums)
        ans = 0
        for key, val in count.items():
            if val % k == 0:
                ans += (key * val)
        return ans