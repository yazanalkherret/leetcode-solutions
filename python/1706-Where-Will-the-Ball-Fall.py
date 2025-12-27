# Time Complexity: O(m * n)
# Space Complexity: O(m * n)

class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        m, n = len(grid), len(grid[0])
        def isWall(j):
            return j < 0 or j >= n
        
        def stuck(i, j):
            if grid[i][j] == 1:
                return isWall(j + 1) or grid[i][j + 1] == -1
            else:
                return isWall(j - 1) or grid[i][j - 1] == 1
                
        def dfs(i, j):
            if isWall(j) or stuck(i, j) :
                return float("-inf")

            if i == m - 1:
                return grid[i][j]

            if grid[i][j] == 1:
                return grid[i][j] + dfs(i + 1, j + 1)

            return grid[i][j] + dfs(i + 1, j - 1)

        ans = []
        for j in range(n):
            displacement = dfs(0, j)
            
            if displacement != float("-inf"):
                ans.append(j + displacement)
            else:
                ans.append(-1)

        return ans
