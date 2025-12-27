# Time Complexity: O(n + m)
# Space Complexity: O(n + m)

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        numToNdx = {}
        nextGreater = [-1] * len(nums2)
        stack = []
        for i, num in enumerate(nums2):
            numToNdx[num] = i
            while stack and num > stack[-1]:
                small = stack.pop()
                nextGreater[numToNdx[small]] = num
            stack.append(num)
        
        ans = []
        for num in nums1:
            ans.append(nextGreater[numToNdx[num]])

        return ans