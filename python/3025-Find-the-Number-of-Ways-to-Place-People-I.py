# Time Complexity: O(n^3)
# Space Complexity: O(1)

class Solution:
    def numberOfPairs(self, points: List[List[int]]) -> int:
        n = len(points)
        validPairs = 0
        for i in range(n):
            x1, y1 = points[i][0], points[i][1]

            for j in range(n):
                x2, y2 = points[j][0], points[j][1]
                if x1 == x2 and y1 == y2: continue
                if not (x1 >= x2 and y2 >= y1): continue

                noneInside = True
                minX, maxX = min(x1, x2), max(x1, x2)
                minY, maxY = min(y1, y2), max(y1, y2)

                for k in range(n):
                    x3, y3 = points[k][0], points[k][1]
                    if (x3, y3) == (x2, y2) or (x3, y3) == (x1, y1): continue

                    if x3 in range(minX, maxX + 1) and y3 in range(minY, maxY + 1):
                        noneInside = False
                        break

                if noneInside:
                    validPairs += 1

        return validPairs