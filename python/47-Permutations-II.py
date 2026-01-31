# Time Complexity: O(n!)
# Space Complexity: O(n)

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        def backtrack(perm, seen):
            if len(perm) == len(nums):
                res.append(perm[:])
                return

            for i in range(len(nums)):
                if i > 0 and nums[i] == nums[i - 1] and i - 1 not in seen:
                    continue

                if i not in seen:
                    seen.add(i)
                    perm.append(nums[i])
                    backtrack(perm, seen)
                    perm.pop()
                    seen.remove(i)

        backtrack([], set())
        return res
