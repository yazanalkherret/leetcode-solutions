# Time Complexity: O(n + q)
# Space Complexity: O(n)

class Solution:
    def treeQueries(self, root: Optional[TreeNode], queries: List[int]) -> List[int]:
        n = self.findLength(root)
        firstOccurence = [None] * (2 * n)
        lastOccurence = [None] * (2 * n)
        order = []
        depth = []
        
        def dfs(curr, level):
            if not curr:
                return

            if not firstOccurence[curr.val]:
                firstOccurence[curr.val] = len(order)

            order.append(curr.val)
            depth.append(level)

            if curr.left:
                dfs(curr.left, level + 1)
                order.append(curr.val)
                depth.append(level)

            if curr.right:
                dfs(curr.right, level + 1)
                order.append(curr.val)
                depth.append(level)

            lastOccurence[curr.val] = len(order)
        
        dfs(root, 0)

        # prefix suffix
        prefixMax = [0] * len(order)
        suffixMax = [0] * len(order)

        for i in range(1, len(order)):
            prefixMax[i] = max(prefixMax[i - 1], depth[i - 1])

        for i in range(len(order) - 2, -1, -1):
            suffixMax[i] = max(suffixMax[i + 1], depth[i + 1])

        ans = []
        for q in queries:
            ans.append(max(prefixMax[firstOccurence[q]], suffixMax[lastOccurence[q]]))

        return ans


    def findLength(self, root):
        if not root:
            return 0
        
        n = 1
        if root.left:
            n += self.findLength(root.left)

        if root.right:
            n += self.findLength(root.right)

        return n