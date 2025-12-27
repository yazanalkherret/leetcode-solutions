# MinHeap Solution

class SmallestInfiniteSet:

    def __init__(self):
        self.heap = [ i + 1 for i in range(1000)]
        self.heapset = set(i + 1 for i in range(1000))
        heapq.heapify(self.heap)

    def popSmallest(self) -> int:
        smallest = heapq.heappop(self.heap)
        print(smallest)
        self.heapset.remove(smallest)
        return smallest

    def addBack(self, num: int) -> None:
        if num not in self.heapset:
            heapq.heappush(self.heap, num)
            self.heapset.add(num)

# Set solution

class SmallestInfiniteSet:

    def __init__(self):
        self.set = set(i + 1 for i in range(1000))

    def popSmallest(self) -> int:
        smallest = min(self.set)
        self.set.remove(smallest)
        return smallest
        
    def addBack(self, num: int) -> None:
        self.set.add(num)

# Optimal Solution

class SmallestInfiniteSet:
    def __init__(self):
        self.smallest = 1
        self.added = set()
    
    def popSmallest(self):
        if self.added:
            res = min(self.added)
            self.added.remove(res)
            return res
        result = self.smallest
        self.smallest += 1
        return result
    
    def addBack(self, num):
        if num < self.smallest:
            self.added.add(num)

