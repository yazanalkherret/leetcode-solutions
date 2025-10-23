from sortedcontainers import SortedList

class TaskManager:

    def __init__(self, tasks: List[List[int]]):
        newOrder = [(p, t, u) for u, t, p in tasks]

        self.tasks = SortedList(newOrder)
        self.user = {}
        self.priority = {}

        for p, t, u in newOrder:
            self.user[t] = u
            self.priority[t] = p

    def add(self, userId: int, taskId: int, priority: int) -> None:
        self.tasks.add((priority, taskId, userId))
        self.user[taskId] = userId
        self.priority[taskId] = priority

    def edit(self, taskId: int, newPriority: int) -> None:
        userId = self.user[taskId]
        self.rmv(taskId)
        self.add(userId, taskId, newPriority)

    def rmv(self, taskId: int) -> None:
        self.tasks.remove((self.priority[taskId], taskId, self.user[taskId]))
        self.user[taskId] = None
        self.priority[taskId] = None

    def execTop(self) -> int:
        if not self.tasks: return -1

        _, _, user = self.tasks.pop()
        return user
