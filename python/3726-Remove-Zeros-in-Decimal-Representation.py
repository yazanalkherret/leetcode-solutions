# Time Complexity: O(logn)
# Space Complexity: O(logn)

class Solution:
    def removeZeros(self, n: int) -> int:
        ans = []
        for char in str(n):
            if char != "0":
                ans.append(char)
        return int("".join(ans))