# Time Complexity: O(N)
# Space Complexity: O(N)

class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        def inorder(root):
            return inorder(root.left) + [(root.val, root)] + inorder(root.right) if root else []

        traversal = inorder(root)
        first_swapped_node, second_swapped_node = None, None

        for i in range(1, len(traversal)):
            if traversal[i][0] < traversal[i - 1][0]:
                if not first_swapped_node:
                    first_swapped_node = traversal[i - 1][1]
                    second_swapped_node = traversal[i][1]
                else:
                    second_swapped_node = traversal[i][1]

        first_swapped_node.val, second_swapped_node.val = second_swapped_node.val, first_swapped_node.val