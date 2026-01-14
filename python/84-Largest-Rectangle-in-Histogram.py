# Time Complexity: O(n)
# Space Complexity: O(n)

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)

        next_smaller = [n] * n
        prev_smaller = [-1] * n

        stack = []
        for i in range(n):
            while stack and heights[stack[-1]] > heights[i]:
                popped_index = stack.pop()
                next_smaller[popped_index] = i

            stack.append(i)

        stack = []
        for i in range(n - 1, -1 , -1):
            while stack and heights[stack[-1]] > heights[i]:
                popped_index = stack.pop()
                prev_smaller[popped_index] = i

            stack.append(i)


        max_rectangle = 0

        for i in range(n):
            curr_rectangle = (next_smaller[i] - prev_smaller[i] - 1) * heights[i]
            max_rectangle = max(max_rectangle, curr_rectangle)

        return max_rectangle
