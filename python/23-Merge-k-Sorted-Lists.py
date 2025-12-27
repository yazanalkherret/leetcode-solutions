# Can be solved many ways

# Time Complexity: O(n log n) -> Sorting
# Space Complexity: O(n) -> array/sorting

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        arr = []
        for curr in lists:
            while curr:
                arr.append(curr.val)
                curr = curr.next

        arr.sort()
        res = ListNode(-1)
        curr = res

        for num in arr:
            curr.next = ListNode(num)
            curr = curr.next
        return res.next