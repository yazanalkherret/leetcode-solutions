class StockSpanner:
    def __init__(self):
        self.counter = 0
        self.decreasing = []
        
    def next(self, price: int) -> int:
        self.counter += 1

        while self.decreasing and price >= self.decreasing[-1][0]:
            self.decreasing.pop()
        
        self.decreasing.append((price, self.counter))
        if len(self.decreasing) == 1: return self.counter

        return self.decreasing[-1][1] - self.decreasing[-2][1]

# Cleaner

class StockSpanner:
    def __init__(self):
        self.stack = []
    
    def next(self, price: int) -> int:
        span = 1
        while self.stack and self.stack[-1][0] <= price:
            span += self.stack.pop()[1]
        self.stack.append((price, span))
        return span