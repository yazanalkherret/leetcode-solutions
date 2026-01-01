# Time Complexity: O(n^2)
# Space Complexity: O(n^2)

class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        two_sum_pairs = Counter()

        for num3 in nums3:
            for num4 in nums4:
                two_sum_pairs[num3 + num4] += 1

        tuples_count = 0

        for num1 in nums1:
            for num2 in nums2:
                tuples_count += two_sum_pairs[-(num1 + num2)]

        return tuples_count
