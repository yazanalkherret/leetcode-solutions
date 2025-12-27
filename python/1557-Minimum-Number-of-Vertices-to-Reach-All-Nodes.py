class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        inDegree = [0] * n

        for src, dest in edges:
            inDegree[dest] += 1

        res = []
        for ndx, v in enumerate(inDegree):
            if not v:
                res.append(ndx)
        return res
