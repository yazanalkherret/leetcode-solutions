class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n + 1)]
        self.rank = [1 for _ in range(n + 1)]
        self.count = n

    def find(self, u):
        res = u
        while res != self.parent[res]:
            self.parent[res] = self.parent[self.parent[res]]
            res = self.parent[res]
        return res

    def union(self, u, v):
        pu, pv = self.find(u), self.find(v)

        if pu == pv: return False

        if self.rank[pu] >= self.rank[pv]:
            self.parent[pv] = pu
            self.rank[pu] += self.rank[pv]
        else:
            self.parent[pu] = pv
            self.rank[pv] += self.rank[pu]


        self.count -= 1
        return True

class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        self.bob = UnionFind(n)
        self.alice = UnionFind(n)
        removed = 0
        for t, u, v in sorted(edges, reverse=True):
            if not self.conditonalUnion(t, u ,v):
                removed += 1

        # Check if connected
        if self.alice.count > 1 or self.bob.count > 1:
            return -1

        return removed
    
    def conditonalUnion(self, t, u, v):
        ALICE, BOB, BOTH = 1, 2, 3

        if t == BOTH:
            res = self.alice.union(u, v)
            res = self.bob.union(u, v) or res
            return res
        elif t == ALICE:
            return self.alice.union(u, v)
        else:
            return self.bob.union(u, v)




