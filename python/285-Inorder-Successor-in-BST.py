# BST
# Time Complexity: Avg: O(logn), Worst: O(n)
# Space Complexity: O(1)

class Solution:    
    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> Optional[TreeNode]:
        successor = None
        while root:
            
            if p.val >= root.val:
                root = root.right
            else:
                successor = root
                root = root.left
                
        return successor

# Any binary tree
# Time Complexity: O(n)
# Space Complexity: O(h)

class Solution:
    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> Optional[TreeNode]:
        previous = None
        successor = None

        def inorder(node):
            nonlocal previous, successor

            if not node:
                return

            inorder(node.left)

            if previous == p:
                successor = node

            previous = node
            inorder(node.right)

        inorder(root)
        return successor
