class Solution:
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        if not (n & 1): return []

        def helper(numOfNodes):
            numOfNodes -= 1
            if numOfNodes == 0:
                return [TreeNode()]

            fullTrees = []
            x, y = numOfNodes - 1, 1
            while y <= numOfNodes:
                # For every left possibility
                # for every right possibility
                # Make a tree and include it
                left = helper(x)
                right = helper(y)
                for i in range(len(left)):
                    for j in range(len(right)):
                        root = TreeNode()
                        root.left = left[i]
                        root.right = right[j]
                        fullTrees.append(root)
                y += 2
                x -= 2

            return fullTrees

        return helper(n)
            