class Leaderboard:

    # SC: O(n)
    def __init__(self):
        self.score = defaultdict(int)
        self.ordered_scores = sortedcontainers.SortedList()

    # TC: O(logn)
    def addScore(self, playerId: int, score: int) -> None:
        if playerId in self.score:
            self.ordered_scores.remove((self.score[playerId], playerId))
            self.score[playerId] += score
            self.ordered_scores.add((self.score[playerId], playerId))
        else:
            self.score[playerId] += score
            self.ordered_scores.add((self.score[playerId], playerId))
            

    # TC: O(k)
    def top(self, K: int) -> int:
        return sum(val for val, _ in self.ordered_scores[-K:])

    # TC: O(logn)
    def reset(self, playerId: int) -> None:
        self.ordered_scores.remove((self.score[playerId], playerId))
        del self.score[playerId]
