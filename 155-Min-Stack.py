# Time Complexity: O(n) for all functions
# Space Complexity: O(n)
class MinStack:

    def __init__(self):
        self.stack = []
        self.min = []

    def push(self, val: int) -> None:
        if not self.stack or self.min[-1] >= val:
            self.min.append(val)

        self.stack.append(val)

    def pop(self) -> None:
        if self.stack[-1] != self.min[-1]:
            return self.stack.pop()
        
        self.min.pop()
        return self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min[-1]

