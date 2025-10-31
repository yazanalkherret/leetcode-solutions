# Time Complexity: O(m*n)
# Space Complexity: O(m*n)

class Solution:
    def zigzagTraversal(self, grid: List[List[int]]) -> List[int]:
        res = []
        for i, row in enumerate(grid):
            res += row[::-1] if i % 2 else row
        return res[::2]