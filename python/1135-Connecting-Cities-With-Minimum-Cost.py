# Time Complexity: O(M logM)
# Space Complexity: O(N)

class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [1 for _ in range(n)]
        self.num_components = n

    def find(self, a):
        a = a - 1
        res = self.parent[a]

        while res != self.parent[res]:
            self.parent[res] = self.parent[self.parent[res]]
            res = self.parent[res]

        return res

    def union(self, a, b) -> bool:
        parent_a, parent_b = self.find(a), self.find(b)

        if parent_a == parent_b:
            return False

        if self.rank[parent_a] >= self.rank[parent_b]:
            self.parent[parent_b] = parent_a
            self.rank[parent_a] += self.rank[parent_b]
        else:
            self.parent[parent_a] = parent_b
            self.rank[parent_b] += self.rank[parent_a]

        self.num_components -= 1

        return True


class Solution:
    def minimumCost(self, n: int, connections: List[List[int]]) -> int:
        sorted_edges = sorted([(cost, a, b) for a, b, cost in connections])        
        union_find = UnionFind(n)
        total_cost = 0

        for cost, a, b in sorted_edges:
            if union_find.union(a, b):
                total_cost += cost

        return total_cost if union_find.num_components == 1 else -1
        