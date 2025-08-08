class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        # Subordinates
        subordinates = defaultdict(list) # Manager -> Employees
        
        # Iinitialize Subordinates
        for i, mngr in enumerate(manager):
            if mngr == -1:
                continue
            subordinates[mngr].append(i)

        def dfs(i, time):
            # Reached end
            if informTime[i] == 0:
                return time

            maxTime = 0
            for sub in subordinates[i]:
                maxTime = max(dfs(sub, time + informTime[i]), maxTime)

            return maxTime

        return dfs(headID, 0)