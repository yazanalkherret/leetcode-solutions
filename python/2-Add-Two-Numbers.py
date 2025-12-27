# Time Complexity: O(max(m,n)). m and n -> the length of l1 and l2 respectively
# Space Complexity: O(1) -> Not couting the returned answer

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        first, second = 0, 0

        i = 0
        while l1:
            first += l1.val * 10 ** i
            l1 = l1.next
            i += 1

        i = 0
        while l2:
            second += l2.val * 10 ** i
            l2 = l2.next
            i += 1

        total = first + second
        head = ListNode(0)
        res = head

        if total == 0: return res

        while total != 0:
            res.next = ListNode(total % 10)
            total //= 10
            res = res.next

        return head.next


# Shorter version

class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummyHead = ListNode(0)
        curr = dummyHead
        carry = 0
        while l1 != None or l2 != None or carry != 0:
            l1Val = l1.val if l1 else 0
            l2Val = l2.val if l2 else 0
            columnSum = l1Val + l2Val + carry
            carry = columnSum // 10
            newNode = ListNode(columnSum % 10)
            curr.next = newNode
            curr = newNode
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return dummyHead.next