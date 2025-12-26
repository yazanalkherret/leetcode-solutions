# Time Complexity: O(N + E)
# Space Complexity: O(N)

class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [1 for _ in range(n)]
        self.components = n

    def find(self, v):
        res = self.parent[v]
        while res != self.parent[res]:
            self.parent[res] = self.parent[self.parent[res]]
            res = self.parent[res]

        return res

    def connected(self, v1, v2):
        return self.find(v1) == self.find(v2)

    def union(self, v1, v2):
        if self.connected(v1, v2): return

        p1, p2 = self.find(v1), self.find(v2)

        if self.rank[p1] >= self.rank[p2]:
            self.parent[p2] = self.parent[p1]
            self.rank[p1] += self.rank[p2]
        else:
            self.parent[p1] = self.parent[p2]
            self.rank[p2] += self.rank[p1]

        self.components -= 1
    

class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        if len(connections) < n - 1: 
            return -1

        union_find = UnionFind(n)

        for a, b in connections:
            union_find.union(a, b)

        return union_find.components - 1
