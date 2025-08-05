class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        # Optimal solution
        
        delta = defaultdict(int)

        for src, dist in trust:
            delta[src] -= 1
            delta[dist] += 1

        for i in range(1, n + 1):
            if delta[i] == n - 1:
                return i
        return -1