# Time Complexity: O(n + k log n)
# Space Complexity: O(n)

import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        res, distances = [], []
        
        for i in range(len(points)):
            x, y = points[i][0], points[i][1]
            distance = sqrt(x ** 2 + y ** 2)
            distances.append([distance, i])

        heapify(distances)

        for _ in range(k):
            d, i = heappop(distances)
            res.append(points[i])

        return res