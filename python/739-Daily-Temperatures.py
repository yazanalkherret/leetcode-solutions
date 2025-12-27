# Time Complexity: O(n)
# Space Complexity: O(n)

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = [] # [[ndx, value]]
        for i, temp in enumerate(temperatures):
            while stack and temp > stack[-1][1]:
                ndx, _ = stack.pop()
                res[ndx] = i - ndx
            stack.append([i, temp])
        return res