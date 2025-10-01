class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [1 for _ in range(n)]
        self.componentsNumber = n

    def find(self, v):
        res = v

        while res != self.parent[res]:
            self.parent[res] = self.parent[self.parent[res]]
            res = self.parent[res]

        return res
    
    def union(self, v1, v2):
        p1, p2 = self.find(v1), self.find(v2)

        if p1 == p2: return False

        if self.rank[p1] > self.rank[p2]:
            self.parent[p2] = p1
            self.rank[p1] += self.rank[p2]
        else:
            self.parent[p1] = p2
            self.rank[p2] += self.rank[p1]

        self.componentsNumber -= 1

        return True

class Solution:
    def maxStability(self, n: int, edges: List[List[int]], k: int) -> int:
        mandatory = []
        optional = []
        uf = UnionFind(n)

        for u, v, w, m in edges:
            if m: mandatory.append((w, u, v))
            else: optional.append((w, u, v))
        
        includedEdges = []
        # Connect Mandatory and check for a cycle:
        for w, u, v in mandatory:
            includedEdges.append([w, 1])
            if not uf.union(u, v):
                return -1

        
        # Max Spanning Tree
        for w, u, v in sorted(optional, reverse = True):
            if uf.union(u, v):
                includedEdges.append([w, 0])

        if uf.componentsNumber > 1: return -1
        includedEdges.sort()

        for i in range(k):
            if i >= len(includedEdges): break

            if not includedEdges[i][1]:
                includedEdges[i][0] *= 2

        return min(includedEdges)[0]


        