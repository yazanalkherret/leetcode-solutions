# Time Complexity: O(n^2) -> The problem does not guarantee that each key appears no more than once across all boxes.
# Space Complexity: O(n)

class Solution:
    def maxCandies(self, status: List[int], candies: List[int], keys: List[List[int]], containedBoxes: List[List[int]], initialBoxes: List[int]) -> int:
        queue = deque()
        foundBoxes = set()
        for box in initialBoxes:
            if status[box]: queue.append(box)
            foundBoxes.add(box)
        
        total = 0
        visited = set()
        
        while queue:
            curr = queue.popleft()

            if curr in visited: continue

            visited.add(curr)

            total += candies[curr]
            
            for box in containedBoxes[curr]:
                foundBoxes.add(box)
                if status[box] and box not in visited:
                    queue.append(box)

            for key in keys[curr]:
                if key in foundBoxes and key not in visited:
                    queue.append(key)
                status[key] = 1

        return total
