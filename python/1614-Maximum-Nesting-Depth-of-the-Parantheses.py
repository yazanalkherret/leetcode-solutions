# Time Complexity: O(n)
# Space Complexity: O(1)

class Solution:
    def maxDepth(self, s: str) -> int:
        open_paran = 0
        res = 0 
        for char in s:
            if char == '(':
                open_paran += 1
                res = max(res, open_paran)
            elif char == ")":
                open_paran -= 1

        return res
