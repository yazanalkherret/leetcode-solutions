# Time Complexity: O(n)
# Space Complexity: O(n)

class Solution:
    def sufficientSubset(self, root: Optional[TreeNode], limit: int) -> Optional[TreeNode]:
        
        def helper(root, pathSum):
            if not root:
                return float("-inf")

            pathSum += root.val

            if not root.right and not root.left:
                return pathSum
            
            left, right = helper(root.left, pathSum), helper(root.right, pathSum)

            if left < limit:
                root.left = None
            if right < limit:
                root.right = None

            return max(left, right)

        placeholder = TreeNode(0)
        placeholder.left = root
        helper(placeholder, 0)
        return placeholder.left

# Elegant

class Solution:
    def sufficientSubset(self, root, limit):
        if not root.left and not root.right:
            return None if root.val < limit else root
        if root.left:
            root.left = self.sufficientSubset(root.left, limit - root.val)
        if root.right:
            root.right = self.sufficientSubset(root.right, limit - root.val)
        return root if root.left or root.right else None