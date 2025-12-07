# No libraries

class ListNode:
    def __init__(self, key=None, value=None):
        self.key = key
        self.val = value
        self.next, self.prev = None, None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.keyNode = {}
        self.first, self.last = ListNode(), ListNode()
        self.first.next = self.last
        self.last.prev = self.first

    def get(self, key: int) -> int:
        if key not in self.keyNode:
            return -1

        targetValue = self.keyNode[key].val
        self.remove(key)
        self.add(key, targetValue)

        return targetValue


    def put(self, key: int, value: int) -> None:
        if key in self.keyNode:
            self.remove(key)
        elif len(self.keyNode) == self.capacity:
            self.removeLRU()

        self.add(key, value)
    
    def remove(self, key):
        targetNode = self.keyNode[key]
        prev, nxt = targetNode.prev, targetNode.next
        prev.next, nxt.prev = nxt, prev
        del self.keyNode[key]

    def add(self, key, value):
        node = ListNode(key, value)
        prev = self.last.prev

        node.next = self.last
        node.prev = prev

        prev.next = node
        self.last.prev = node

        self.keyNode[key] = node

    def removeLRU(self):
        LRU = self.first.next
        nextLRU = LRU.next
        self.first.next = nextLRU
        nextLRU.prev = self.first

        del self.keyNode[LRU.key]
