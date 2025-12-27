# Time Complexity: O(n logn) -> Sorting
# Space Complexity: O(n) -> Dictionary and Timsort

class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        traverse = defaultdict(list)

        def dfs(node, col, row):
            if not node: return

            traverse[col].append((row, node.val))
            dfs(node.left, col - 1, row + 1)
            dfs(node.right, col + 1, row + 1)

        dfs(root, 0, 0)
        res = []

        for key in sorted(traverse):
            col = []
            for _, nodeVal in sorted(traverse[key]):
                col.append(nodeVal)

            res.append(col)

        return res