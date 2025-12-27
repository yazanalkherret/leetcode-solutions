class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        status = {} # Bool, safe or unsafe
        res = []

        def dfs(i):
            if i in status:
                return status[i]
            status[i] = False
            for nghbr in graph[i]:
                if not dfs(nghbr):
                    return status[i] # False
            status[i] = True # All neighbors are safe
            return status[i]

        for i in range(len(graph)):
            if dfs(i):
                res.append(i)

        return res