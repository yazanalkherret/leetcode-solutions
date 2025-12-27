class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        
        prereq = defaultdict(set) # Course -> Prerequisites

        # Indegrees and Adj
        indegree = [0] * numCourses
        adj = defaultdict(set)
        for src, dest in prerequisites:
            indegree[dest] += 1
            adj[src].add(dest)

        # Modified Topological Sort
        queue = deque([i for i in range(numCourses) if indegree[i] == 0])
        while queue:
            curr = queue.popleft()

            for nei in adj[curr]:
                indegree[nei] -= 1

                prereq[nei].update(prereq[curr])
                prereq[nei].add(curr)

                if indegree[nei] == 0:
                    queue.append(nei)

        # Query Results
        res = []

        for u, v in queries:
            if u in prereq[v]:
                res.append(True)
            else:
                res.append(False)

        return res

        