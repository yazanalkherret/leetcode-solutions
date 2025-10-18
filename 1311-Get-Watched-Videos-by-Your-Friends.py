# Time Complexity: O(n + m + v logv)
# Space Complexity: O(n + m + v)

class Solution:
    def watchedVideosByFriends(self, watchedVideos: List[List[str]], friends: List[List[int]], id: int, level: int) -> List[str]:
        n = len(friends)
        adj = [[] for _ in range(n)]

        # Adjacency List Construction
        for i in range(n):
            for j in range(len(friends[i])):
                adj[i].append(friends[i][j])

        # BFS
        queue = deque([(id, 0)])
        seen = set()
        distances = [float("inf")] * n
        while queue:
            person, currDistance = queue.popleft()
            if person in seen: continue

            seen.add(person)
            distances[person] = currDistance 

            for friend in adj[person]:
                if friend in seen: continue

                queue.append((friend, currDistance + 1))

        freqVids = defaultdict(int)
        for friend, distance in enumerate(distances):
            if distance == level:
                for watchedVid in watchedVideos[friend]:
                    freqVids[watchedVid] += 1

        # Return value -> Video ordered by frequency, alphabetically -> increasing
        return [vid for freq, vid in sorted([(freq, vid) for vid, freq in freqVids.items()])]