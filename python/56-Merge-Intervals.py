# Time Complexity: O(n log n) for sorting
# Space Complexity: O(n) for sorting and for stack

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        stack = []

        for start, end in intervals:

            if stack and start <= stack[-1][1]:
                # Merge
                lastStart, lastEnd = stack.pop()
                start = lastStart
                end = max(end, lastEnd)

            stack.append([start, end])

        return stack