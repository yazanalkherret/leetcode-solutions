class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        minn = min(nums)
        maxx = max(nums)

        present = set(nums)
        ans = []
        for i in range(minn, maxx + 1):
            if i not in present:
                ans.append(i)
        return ans