# Time Complexity: O(n)
# Space Complexity: O(h)

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.good_nodes = 0

        def helper(node, max_in_path):
            if not node:
                return

            if node.val >= max_in_path:
                self.good_nodes += 1

            helper(node.left, max(max_in_path, node.val))
            helper(node.right, max(max_in_path, node.val))

        helper(root, root.val)
        return self.good_nodes
