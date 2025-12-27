# Time Complexity: O(n + hlogh)
# Space Complexity: O(n + h)

class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        sums = []
        queue = deque([root])

        while queue:
            sumLevel = 0
            for _ in range(len(queue)):
                node = queue.popleft()
                sumLevel += node.val

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            sums.append(sumLevel)

        if k > len(sums): return -1
        return sorted(sums, reverse=True)[k - 1] 