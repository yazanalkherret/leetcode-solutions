# Time Complexity: O(n)
# Space Complexity: O(n)

class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        self.helper(head, None)
        return head

    def helper(self, node, parent):
        if not node:
            return
            
        node.prev = parent
        temp = node.next
        last = node
        
        if node.child:
            last = self.helper(node.child, node)
            node.next = node.child
            node.child = None
        
        last.next = temp
        if last.next:
            last = self.helper(last.next, last)

        return last
