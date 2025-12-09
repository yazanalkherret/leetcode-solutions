# Time Complexity: O(n)
# Auxiliary Space Complexity: O(1) 

class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        res = []
        currNum = 0
        for currTargetNum in target:
            for _ in range(currTargetNum - currNum - 1):
                res.append("Push")
                res.append("Pop")
            res.append("Push")
            currNum = currTargetNum
        return res
