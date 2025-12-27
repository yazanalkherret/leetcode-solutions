# Time Complexity: O(n)
# Space Complexity: O(1)

class Solution:
    def edgeScore(self, edges: List[int]) -> int:
        n = len(edges)
        scores = [0] * n
        maxScore = 0
        indexMaxScore = 0 
        
        for src, dest in enumerate(edges):
            scores[dest] += src

            if scores[dest] > maxScore:
                maxScore = scores[dest]
                indexMaxScore = dest

            elif scores[dest] == maxScore and dest < indexMaxScore:
                maxScore = scores[dest]
                indexMaxScore = dest
                
        return indexMaxScore