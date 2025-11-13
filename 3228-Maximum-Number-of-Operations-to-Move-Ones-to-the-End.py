# Time Complexity: O(n)
# Space Complexity: O(1)

class Solution:
    def maxOperations(self, s: str) -> int:
        operations = 0
        numOnes, lastOneNdx = 0, float("inf")
        for i, char in enumerate(s):
            if char == "1":
                if lastOneNdx < i - 1:
                    operations += numOnes
                numOnes += 1
                lastOneNdx = i

        operations += numOnes if s[-1] == "0" else 0
        return operations
