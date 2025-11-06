from sortedcontainers import SortedList

class UnionFind:
    def __init__(self, c):
        self.parent = [i for i in range(c + 1)]
        self.rank = [1 for i in range(c + 1)]
        self.onlineByParent = [SortedList() for _ in range(c + 1)]

    def find(self, v):
        res = v
        while res != self.parent[res]:
            self.parent[res] = self.parent[self.parent[res]]
            res = self.parent[res]
        return res

    def union(self, v1, v2):
        p1, p2 = self.find(v1), self.find(v2)
        if p1 == p2: return

        if self.rank[p1] >= self.rank[p2]:
            self.parent[p2] = p1
            self.rank[p1] += self.rank[p2]
        else:
            self.parent[p1] = p2
            self.rank[p2] += self.rank[p1]

    def constructGrid(self, c):
        for i in range(1, c + 1):
            parent = self.find(i)

            if not self.onlineByParent[parent].__contains__(i):
                self.onlineByParent[parent].add(i)
      
    def check(self, v):
        parent = self.find(v)

        if not self.onlineByParent[parent]:
            return -1
        
        if self.onlineByParent[parent].__contains__(v):
            return v

        return self.onlineByParent[parent][0]


    def offline(self, v):
        parent = self.find(v)
        self.onlineByParent[parent].discard(v)

class Solution:
    def processQueries(self, c: int, connections: List[List[int]], queries: List[List[int]]) -> List[int]:
        uf = UnionFind(c)

        for v1, v2 in connections:
            uf.union(v1, v2)

        uf.constructGrid(c)
        
        ans = []

        for queryType, v in queries:
            if queryType == 1:
                ans.append(uf.check(v))
            else:
                uf.offline(v)

        return ans