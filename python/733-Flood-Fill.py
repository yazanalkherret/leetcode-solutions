# Time Complexity: O(m * n)
# Space Complexity: O(m * n)

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        original_color = image[sr][sc]
        if original_color == color: return image
        
        m, n = len(image), len(image[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def dfs(row, col):
            image[row][col] = color

            for dr, dc in directions:
                nei_r, nei_c = row + dr, col + dc

                if (0 <= nei_r < m and 0 <= nei_c < n and 
                    image[nei_r][nei_c] == original_color):

                    dfs(nei_r, nei_c)

        dfs(sr, sc)
        return image
