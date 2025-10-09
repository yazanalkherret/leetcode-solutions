# Time Complexity: O(n + m)
# Space Complexity: O(n + m)

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        count1, count2 = Counter(nums1), Counter(nums2)
        ans = []
        for num in count1:
            if num in count2:
                for x in range(min(count1[num], count2[num])):
                    ans.append(num)

        return ans