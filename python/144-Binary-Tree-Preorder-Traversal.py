# Iterative
# Time Complexity: O(n)
# Space Complexity: O(n)

class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # Iterative
        res = []
        stack = [root]
        while stack:
            cur = stack.pop()
            if not cur: continue

            res.append(cur.val)
            stack.append(cur.right)
            stack.append(cur.left)

        return res