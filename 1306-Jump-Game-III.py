class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        
        def inBounds(i):
            return 0 <= i < len(arr)

        # BFS
        queue = deque()
        queue.append(start)
        visited = [0] * len(arr)
        visited[start] = 1

        while queue:
            curr = queue.popleft()

            if not arr[curr]:
                return True

            neighbors = [curr + arr[curr], curr - arr[curr]]
            for nei in neighbors:
                if inBounds(nei) and not visited[nei]:
                    queue.append(nei)
                    visited[nei] = 1

        return False