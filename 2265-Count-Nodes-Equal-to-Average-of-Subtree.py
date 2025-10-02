# Time Complexity: O(n)
# Space Complexity: O(n)

class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        if not root: return 0

        return self.dfs(root)[2]

    def dfs(self, root):
        if not root:
            return (0, 0, 0) # SubtreeTotal, NumOfNodes, Avg

        leftTotal, leftNodes, leftRes = self.dfs(root.left)
        rightTotal, rightNodes, rightRes = self.dfs(root.right)

        currTotal = leftTotal + rightTotal + root.val
        numNodes = leftNodes + rightNodes + 1
        currAvg = currTotal // numNodes
        currRes = leftRes + rightRes

        if root.val == currAvg:
            currRes += 1

        return (currTotal, numNodes, currRes)