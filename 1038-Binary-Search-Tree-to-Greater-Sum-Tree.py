# Time Complexity: O(n)
# Space Complexity: O(n)

class Solution:
    def bstToGst(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        currSum = 0

        def dfs(root):
            nonlocal currSum
            if not root:
                return 0

            dfs(root.right)
            currSum += root.val
            root.val = currSum
            dfs(root.left)

        dfs(root)
        return root
