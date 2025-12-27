# The following is a BFS solution
# It is possible to solve it with DFS too

class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        nbrs = defaultdict(list)
        # Initialize neighbors
        # Vertix(V)-> Neighbor, Flag
        # Flag -> 0 : Outgoing from V, -> 1: Ingoing into V

        for connection in connections:
            outgoing, ingoing = connection[0], connection[1] 
            nbrs[outgoing].append([ingoing, 0])
            nbrs[ingoing].append([outgoing, 1])

        
        # Figure out number of flips
        count = 0
        visited = set()
        q = deque()
        q.append(0)

        while q:
            curr = q.popleft()
            visited.add(curr)
            for nei in nbrs[curr]:
                if nei[0] in visited:
                    continue
                # If neighbor is NOT ingoing into the parent
                if not nei[1]: 
                    count += 1
                q.append(nei[0])
        
        return count