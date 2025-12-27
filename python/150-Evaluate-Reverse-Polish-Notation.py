# Time Complexity: O(n)
# Space Complexity: O(n)

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = set(['+', '-', '/', '*'])

        def calcRes(first, second, operator):
            if operator == '+':
                return second + first
            elif operator == '-':
                return second - first
            elif operator == '*':
                return second * first
            else:
                return int(second / first) # Truncate to zero

        for char in tokens:
            if char in operators:
                first, second = stack.pop(), stack.pop()
                result = calcRes(first, second, char)
                stack.append(result)
            else:
                stack.append(int(char))

        return stack[-1]