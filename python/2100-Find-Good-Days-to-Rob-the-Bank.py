# Time Complexity: O(n)
# Space Complexity: O(n)

class Solution:
    def goodDaysToRobBank(self, security: List[int], time: int) -> List[int]:
        n = len(security)
        noninc = [1] * n
        nondec = [1] * n
        
        for i in range(1, n):
            if security[i] <= security[i - 1]:
                noninc[i] += noninc[i - 1]
            if security[i] >= security[i - 1]:
                nondec[i] += nondec[i - 1]
             
        ans = []
        for i in range(time, n - time):
            if noninc[i] >= time + 1 and nondec[i + time] >= time + 1:
                ans.append(i)

        return ans