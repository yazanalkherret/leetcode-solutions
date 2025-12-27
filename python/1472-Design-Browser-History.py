class ListNode:
    def __init__(self, url, prev = None, next = None):
        self.url = url
        self.prev = prev
        self.next = next

class BrowserHistory:

    def __init__(self, homepage: str):
        self.current = ListNode(homepage)

    def visit(self, url: str) -> None:
        if self.current.next:
            self.current.next.prev = None # Clear
        self.current.next = ListNode(url, self.current)
        self.forward(1) 

    def back(self, steps: int) -> str:
        i = 0
        while i < steps and self.current.prev:
            self.current = self.current.prev
            i += 1
        return self.current.url
    def forward(self, steps: int) -> str:
        i = 0
        while i < steps and self.current.next:
            self.current = self.current.next
            i += 1
        return self.current.url