# Time Complexity: O(n)
# Space Complexity: O(n)

class Solution:
    def __init__(self):
        self.graph = defaultdict(list)

    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        self.build_graph(root, None)

        res = []
        queue = deque([(target.val, 0, None)])
        while queue:

            if queue[0][1] > k:
                break

            cur, distance, parent = queue.popleft()
                
            if distance == k:
                res.append(cur)

            for nei in self.graph[cur]:
                if nei != parent:
                    queue.append((nei, distance + 1, cur))

        return res

    def build_graph(self, root, parent):
        if not root:
            return

        if parent:
            self.graph[root.val].append(parent.val)
            self.graph[parent.val].append(root.val)
        
        self.build_graph(root.left, root)
        self.build_graph(root.right, root)
