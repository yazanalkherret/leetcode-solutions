class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        exists = set(nums)
        curr = k
        for i in range(1, 102):
            curr = k * i
            if curr not in exists:
                return curr