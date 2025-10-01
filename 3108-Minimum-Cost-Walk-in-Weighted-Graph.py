class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [1 for _ in range(n)]
        self.weight = [~0 for i in range(n)]

    def find(self, v):
        res = v
        while res != self.parent[res]:
            self.parent[res] = self.parent[self.parent[res]]
            res = self.parent[res]
        return res

    def same(self, v1, v2):
        return self.find(v1) == self.find(v2)

    def union(self, v1, v2, w):
        p1, p2 = self.find(v1), self.find(v2)

        if p1 == p2:
            self.weight[p1] &= w
            return

        if self.rank[p1] >= self.rank[p2]:
            self.parent[p2] = p1
            self.rank[p1] += self.rank[p2]
            self.weight[p1] &= w & self.weight[p2]
        else:
            self.parent[p1] = p2
            self.rank[p2] += self.rank[p1]
            self.weight[p2] &= w & self.weight[p1]


class Solution:
    def minimumCost(self, n: int, edges: List[List[int]], query: List[List[int]]) -> List[int]:
        uf = UnionFind(n)
        for v1, v2, w in edges:
            uf.union(v1, v2, w)

        res = []
        for v1, v2 in query:
            if uf.same(v1, v2):
                res.append(uf.weight[uf.find(v1)])
            else:
                res.append(-1)

        return res