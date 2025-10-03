# Time Complexity: O(n+m)
# Space Complexity: O(n)

class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        # Target: indegree = 0
        # If there are multiple, return -1
        indegree = [0] * n

        for src, dest in edges:
            indegree[dest] += 1
        
        targets = []

        for i in range(n):
            if not indegree[i]:
                targets.append(i)

        return targets[0] if len(targets) == 1 else -1