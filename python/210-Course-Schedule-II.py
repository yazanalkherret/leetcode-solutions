class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indegree = [0] * numCourses
        neighbors = defaultdict(list)

        for course, prereq in prerequisites:
            indegree[course] += 1
            neighbors[prereq].append(course)
        
        # Kahn's Algo
        
        queue = deque()
        for i in range(len(indegree)):
            if not indegree[i]:
                queue.append(i) 
        
        order = []
        i = 0
        while queue:
            curr = queue.popleft()
            order.append(curr)
            i += 1

            for nei in neighbors[curr]:
                indegree[nei] -= 1
                if not indegree[nei]:
                    queue.append(nei)

        if i != numCourses:
            return []

        return order