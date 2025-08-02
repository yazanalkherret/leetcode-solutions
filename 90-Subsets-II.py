class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        def backtrack(ndx, path):
            if ndx >= len(nums):
                res.append(path[::])
                return

            path.append(nums[ndx])
            backtrack(ndx + 1, path)
            path.pop()

            j = ndx + 1
            while j < len(nums) and nums[j] == nums[ndx]:
                j += 1
            backtrack(j, path)

        backtrack(0, [])
        return res