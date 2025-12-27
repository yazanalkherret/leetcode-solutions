# Time Complexity: O(n*b + b)
# Space Complexity O(b)

class Solution:
    def largestCombination(self, candidates: List[int]) -> int:
        numOfOnes = [0] * 24

        for i in range(24):
            for j in range(len(candidates)):
                numOfOnes[i] += candidates[j] & 1
                candidates[j] >>= 1

        return max(numOfOnes)