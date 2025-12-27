class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegree = [0] * numCourses
        children = defaultdict(list)

        for course, prereq in prerequisites:
            indegree[course] += 1
            children[prereq].append(course)

        queue = deque()
        for i in range(len(indegree)):
            if not indegree[i]:
                queue.append(i)

        i = 0
        while queue:
            curr = queue.popleft()
            i += 1

            for child in children[curr]:
                indegree[child] -= 1
                if not indegree[child]:
                    queue.append(child)

        return i == numCourses