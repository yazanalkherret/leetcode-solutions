# Time Complexity: O(m+n)
# Space Complexity: O(1)

class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        res = 0

        # len(nums1) odd
        if len(nums1) % 2 != 0:
            # XOR nums2
            for num in nums2:
                res ^= num

        # len(nums2) odd
        if len(nums2) % 2 != 0:
            # XOR nums1
            for num in nums1:
                res ^= num

        return res
