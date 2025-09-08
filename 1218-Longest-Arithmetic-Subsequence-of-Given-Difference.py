# Time Complexity: O(n)
# Space Complexity: O(n)

class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        N = len(arr)
        memo = [0] * N
        numNdx = {}

        for ndx, num in enumerate(arr):
            target = num - difference
            if target in numNdx and numNdx[target] < ndx:
                memo[ndx] = memo[numNdx[target]] + 1
            else:
                memo[ndx] = 1
            numNdx[num] = ndx
        return max(memo)


# Better solution

class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        length = dict()
        for num in arr:
                length[num] = length.get(num - difference, 0) + 1
        return max(length.values())