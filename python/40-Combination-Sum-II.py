class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        def backtrack(i, total, path):
            if total == target:
                res.append(path[::])
                return

            if i == len(candidates):
                return

            # Include candidates[i]
            if total + candidates[i] <= target:
                path.append(candidates[i])
                backtrack(i + 1, total + candidates[i], path)
                path.pop()

            # Don't include candidates[i]

            # Solve duplicate problem
            while i + 1 < len(candidates) and candidates[i] == candidates[i+1]:
                i += 1

            backtrack(i + 1, total, path)

        backtrack(0, 0, [])
        return res