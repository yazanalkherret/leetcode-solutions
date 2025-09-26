# Time Complexity: O(m + nlogn)
# Space Complexity: O(n)

class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        degrees = [0] * n
        currVal = n
        res = 0
        for v1, v2 in roads:
            degrees[v1] += 1
            degrees[v2] += 1
           
        for degree in sorted(degrees, reverse=True):
            res += currVal * degree
            currVal -= 1

        return res