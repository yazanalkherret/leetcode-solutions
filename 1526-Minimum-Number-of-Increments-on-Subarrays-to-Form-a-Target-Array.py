# Time Complexity: O(n)
# Space Complexity: O(1)

class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        res = target[0]
        for i in range(len(target) - 1):
            if target[i + 1] > target[i]:
                res += target[i + 1] - target[i]

        return res