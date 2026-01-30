# Time Complexity: O(nlogk)
# Space Complexity: O(k)

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        head = ListNode()

        # Node Mapping
        val_node_map = defaultdict(list)
        heap = []
        for node in lists:
            if node:
                heappush(heap, node.val)
                val_node_map[node.val].append(node)

        
        res_ptr = head

        while heap:
            val = heappop(heap)
            
            node = val_node_map[val].pop()

            # Add to res
            res_ptr.next = ListNode(val)
            res_ptr = res_ptr.next

            if node.next:
                heappush(heap, node.next.val)
                val_node_map[node.next.val].append(node.next)

        return head.next

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