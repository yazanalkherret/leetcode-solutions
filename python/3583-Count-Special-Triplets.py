# Time Complexity: O(n)
# Space Complexity: O(n)

class Solution:
    def specialTriplets(self, nums: List[int]) -> int:
        n = len(nums)
        MOD = 10 ** 9 + 7
        freq = defaultdict(int)
        prev, after = [0] * n, [0] * n
        
        for i, num in enumerate(nums):
            prev[i] = freq[num * 2]
            freq[num] += 1

        freq = defaultdict(int)

        for i in range(n - 1, -1, -1):
            after[i] = freq[nums[i] * 2]
            freq[nums[i]] += 1

        special_triplets = 0

        for i in range(n):
            special_triplets = (special_triplets + prev[i] * after[i]) % MOD

        return special_triplets 
