class OrderedStream:

    # Time Complexity: O(n)
    # Space Complexity: O(n)

    def __init__(self, n: int):
        self.ptr = 0
        self.stream = [None] * n

    # Time Complexity: amortized(1)
    # Space Complexity: O(1)
    
    def insert(self, idKey: int, value: str) -> List[str]:
        idKey -= 1
        self.stream[idKey] = value

        chunk = []

        while self.ptr < len(self.stream) and self.stream[self.ptr]:
            chunk.append(self.stream[self.ptr])
            self.ptr += 1

        return chunk 
