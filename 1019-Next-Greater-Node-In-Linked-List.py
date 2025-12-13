# Time Complexity: O(n)
# Space Complexity: O(n)

class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        stack, res = [], []

        i, curr = 0, head
        while curr:
            res.append(0)

            while stack and stack[-1][0] < curr.val:
                _, ndx = stack.pop()
                res[ndx] = curr.val

            stack.append((curr.val, i))
            curr = curr.next
            i += 1

        return res
