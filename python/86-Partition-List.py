# Time Complexity: O(n)
# Space Complexity: O(1)

class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        s1 = e1 = ListNode()
        s2 = e2 = ListNode()

        curr = head
        while curr:
            if curr.val < x:
                # partition 1
                e1.next = curr
                e1 = e1.next
            else:
                # partition 2
                e2.next = curr
                e2 = e2.next

            curr = curr.next

        e2.next = None
        e1.next = s2.next

        return s1.next
