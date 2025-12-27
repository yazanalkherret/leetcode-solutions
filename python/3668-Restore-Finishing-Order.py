class Solution:
    def recoverOrder(self, order: List[int], friends: List[int]) -> List[int]:
        personOrder = { p : i for i, p in enumerate(order)}
        friendsWithOrder = []
        for friend in friends:
            friendsWithOrder.append((personOrder[friend], friend))

        return [ f for o, f in sorted(friendsWithOrder)]