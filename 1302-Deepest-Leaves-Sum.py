# Time Complexity: O(n)
# Space Complexity: O(h)

class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        self.res = defaultdict(list)
        self.dfs(root, 0)
        return sum(self.res[max(self.res.keys())])


    def dfs(self, root, depth):
        if not root.right and not root.left:
            self.res[depth].append(root.val)
            return

        if root.right:
            self.dfs(root.right, depth + 1)

        if root.left:
            self.dfs(root.left, depth + 1)
