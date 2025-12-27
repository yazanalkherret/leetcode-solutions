class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        res = [-1] * n
        visited = set()
        neighbors = defaultdict(list)

        for src, dest in redEdges:
            neighbors[src].append((dest, 'red'))

        for src, dest in blueEdges:
            neighbors[src].append((dest, 'blue'))

        # BFS
        queue = collections.deque()
        queue.append((0, 'zero'))
        visited.add((0, 'zero'))
        step = 0

        while queue:
            curr_level = []
            for _ in range(len(queue)):
                curr_level.append(queue.popleft())
            
            for curr_node, curr_color in curr_level:
                if res[curr_node] == -1:
                    res[curr_node] = step 
                for new_node, new_color in neighbors[curr_node]:
                    if (new_node, new_color) not in visited and new_color != curr_color:
                        queue.append((new_node, new_color))
                        visited.add((new_node, new_color))

            step += 1
        return res