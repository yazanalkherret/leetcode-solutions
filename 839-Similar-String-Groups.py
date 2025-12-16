# Time Complexity: O(n^2 * m)
# Space Complexity: O(n)

class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [1 for _ in range(n)]
        self.num_groups = n
    
    def find(self, v):
        while v != self.parent[v]:
            self.parent[v] = self.parent[self.parent[v]]
            v = self.parent[v]
        return v

    def union(self, v1, v2):
        p1, p2 = self.find(v1), self.find(v2)
        if p1 == p2: return

        self.num_groups -= 1

        if self.rank[p1] >= self.rank[p2]:
            self.parent[p2] = p1
            self.rank[p1] += self.rank[p2]
        else:
            self.parent[p1] = p2
            self.rank[p2] += self.rank[p1]

class Solution:
    def numSimilarGroups(self, strs: List[str]) -> int:
        n = len(strs)

        def areSimilar(w1, w2):
            differences = 0

            for i in range(len(w1)):
                if w1[i] != w2[i]:
                    differences += 1
                if differences > 2:
                    return False

            return differences in (0, 2)

        uf = UnionFind(n)

        for i in range(n):
            for j in range(i + 1, n):
                if areSimilar(strs[i], strs[j]):
                    uf.union(i, j)

        return uf.num_groups
