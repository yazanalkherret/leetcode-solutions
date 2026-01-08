# Time Complexity: O(n)
# Space Complexity: O(1)

class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head: return

        # Get length and tail
        list_len, tail = 0, None

        cur = head
        while cur:
            list_len += 1
            if not cur.next:
                tail = cur
            cur = cur.next

        
        k = k % list_len

        # Edge case: Full/No rotation
        if k == 0: return head
        
        pivot_parent = None
        pivot_node = head

        for _ in range(list_len - k):
            pivot_parent = pivot_node
            pivot_node = pivot_node.next

        pivot_parent.next = None
        tail.next = head
        head = pivot_node

        return head
