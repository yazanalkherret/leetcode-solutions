# Time Complexity: O(n)
# Space Complexity: O(n)

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        def helper(left, right):
            nonlocal preorder_index

            if left > right:
                return

            cur_val = preorder[preorder_index]
            cur_node = TreeNode(cur_val)
            preorder_index += 1

            cur_node.left = helper(left, node_indices[cur_val] - 1)
            cur_node.right = helper(node_indices[cur_val] + 1, right)

            return cur_node
        
        node_indices = {node : i for i, node in enumerate(inorder)}
        preorder_index = 0
        return helper(0, len(preorder) - 1)
