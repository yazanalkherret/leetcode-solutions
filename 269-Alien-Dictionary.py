class Solution:
    def alienOrder(self, words: List[str]) -> str:
        n = len(words)
        unique_chars = set(char for word in words for char in word)
        adj = defaultdict(list)
        indegree = { char : 0 for char in unique_chars }

        # Construct relationships
        for i in range(n):
            for j in range(i + 1, n):
                
                if len(words[i]) > len(words[j]) and words[i].startswith(words[j]):
                    return ""

                for k in range(min(len(words[i]), len(words[j]))):
                    if words[i][k] != words[j][k]:
                        adj[words[i][k]].append(words[j][k])
                        indegree[words[j][k]] += 1
                        break
        
        # Top Sort
        queue = deque()
        for char, degree in indegree.items():
            if not degree:
                queue.append(char)
        res = []
        while queue:
            curr_char = queue.popleft()
            res.append(curr_char)

            for next_char in adj[curr_char]:
                indegree[next_char] -= 1
                if not indegree[next_char]:
                    queue.append(next_char)

        return "" if len(res) != len(unique_chars) else "".join(res)
