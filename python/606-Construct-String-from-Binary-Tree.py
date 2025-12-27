# Time Complexity: O(n)
# Space Complexity: O(n)

class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        self.ans = []
        self.helper(root)
        return "".join(self.ans)

    def helper(self, root):
            self.ans.append(str(root.val))
            if root.left:
                self.ans.append("(")
                self.helper(root.left)
                self.ans.append(")")

            if root.right:
                if not root.left:
                    self.ans.append("()")
                self.ans.append("(")
                self.helper(root.right)
                self.ans.append(")")