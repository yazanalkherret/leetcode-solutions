# Time Complexity: O(n * h)
# Space Complexity: O(h)

class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        all_paths = []
        
        def dfs_path(root, path):
            if root:
                path.append(str(root.val))
            
            if not root.left and not root.right:
                all_paths.append("".join(path))
                path.pop()
                return

            if root.left:
                path.append("->")
                dfs_path(root.left, path)
                path.pop()

            if root.right:
                path.append("->")
                dfs_path(root.right, path)
                path.pop()

            path.pop()

        dfs_path(root, [])
        return all_paths
