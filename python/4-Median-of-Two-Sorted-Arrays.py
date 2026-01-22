# Time Complexity: O(log(min(m, n)))
# Space Complexity: O(1)

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        total_len = len(nums1) + len(nums2)
        part_len = total_len // 2

        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        left, right = -1, len(nums1) - 1
        while left <= right:
            i = (left + right) // 2
            j = part_len - i - 2

            nums1_border = nums1[i] if i >= 0 else float("-inf")
            nums2_border = nums2[j] if j >= 0 else float("-inf")

            nums1_cross_border = nums1[i + 1] if i < len(nums1) - 1 else float("inf")
            nums2_cross_border = nums2[j + 1] if j < len(nums2) - 1 else float("inf")

            if nums1_border <= nums2_cross_border and nums2_border <= nums1_cross_border:
                # Found median
                # Odd
                if total_len % 2:
                    return min(nums1_cross_border, nums2_cross_border)

                # Even
                return (
                        (max(nums1_border, nums2_border) +
                        min(nums1_cross_border, nums2_cross_border)) / 2
                    )
                
            elif nums1_border > nums2_cross_border:
                right = i - 1
            else:
                # nums2_border > nums1_corss_border
                left = i + 1

        return 0
