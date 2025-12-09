# Time Complexity: O(n)
# Space Complexity: O(n)

class Solution:
    def getImportance(self, employees, id):
        employeeMap = {e.id: e for e in employees}
        def dfs(employeeId):
            employee = employeeMap[employeeId]
            return (employee.importance +
                    sum(dfs(employeeId) for employeeId in employee.subordinates))
        return dfs(id)
