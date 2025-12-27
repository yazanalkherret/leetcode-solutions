class Solution:
    def minimumOperations(self, nums: List[int], start: int, goal: int) -> int:
        queue = deque([(start, 0)])
        seen = set()

        while queue:
            curr, distance = queue.popleft()
            if curr in seen: continue
            
            if curr == goal: return distance

            if curr < 0 or curr > 1000: continue
            
            seen.add(curr)
            for num in nums:
                queue.append((curr + num, distance + 1))
                queue.append((curr - num, distance + 1))
                queue.append((curr ^ num, distance + 1))

        return -1
                