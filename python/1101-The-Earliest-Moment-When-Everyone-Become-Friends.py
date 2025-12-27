# Time Complexity: O(N + MlogM + Mα(N))
# Space Complexity: O(N + M)

class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [1 for _ in range(n)]
        self.largest_component = 1
    
    def find(self, v):
        while v != self.parent[v]:
            self.parent[v] = self.parent[self.parent[v]]
            v = self.parent[v]
        return v

    def union(self, v1, v2):
        p1, p2 = self.find(v1), self.find(v2)
        if p1 == p2: return

        if self.rank[p1] >= self.rank[p2]:
            self.parent[p2] = p1
            self.rank[p1] += self.rank[p2]
        else:
            self.parent[p1] = p2
            self.rank[p2] += self.rank[p1]

        self.largest_component = max(self.largest_component, self.rank[p1], self.rank[p2])


class Solution:
    def earliestAcq(self, logs: List[List[int]], n: int) -> int:
        unionfind = UnionFind(n)

        for time, x, y in sorted(logs):
            unionfind.union(x, y)

            if unionfind.largest_component == n:
                return time

        return -1
