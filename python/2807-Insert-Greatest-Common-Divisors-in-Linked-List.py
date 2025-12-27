# Time Complexity: O(n * log(min(a, b)))
# Space Complexity: O(1)

class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        l, r = head, head.next

        while r:
            gcdNode = ListNode(gcd(l.val, r.val))
            l.next = gcdNode
            gcdNode.next = r
            l = r
            r = r.next

        return head