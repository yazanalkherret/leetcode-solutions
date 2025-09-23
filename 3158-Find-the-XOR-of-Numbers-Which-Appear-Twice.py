# Time Complexity: O(n)
# Space Complexity: O(n)

class Solution:
    def duplicateNumbersXOR(self, nums: List[int]) -> int:
        freqs = Counter(nums)
        res = 0
        for num, freq in freqs.items():
            if freq > 1:
                res ^= num
        
        return res

# One-liner

class Solution:
    def duplicateNumbersXOR(self, nums: List[int]) -> int:
        return reduce(xor, nums + list(set(nums)))