# Time Complexity: O(n)
# Space Complexity: O(n)

class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        queue = deque([root])
        
        level = 0
        while queue:
            order = [node.val for node in queue]
            if level & 1:
                order.reverse()

            for i in range(len(queue)):
                curr = queue.popleft()
                curr.val = order[i]
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
                    
            level += 1
                
        return root