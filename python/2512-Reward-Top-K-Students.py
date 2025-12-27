# Time Complexity: O(p + q + n * (m + log n) + k log n) -> m: avg num of words in report[]
# Space Complexity: O(p + q + n) -> p, q: pstv, ngtv

class Solution:
    def topStudents(self, positive_feedback: List[str], negative_feedback: List[str], report: List[str], student_id: List[int], k: int) -> List[int]:
        n = len(report)
        positive_feedback, negative_feedback = set(positive_feedback), set(negative_feedback)

        maxHeap = []

        for i, sentence in enumerate(report):
            score = 0
            words = sentence.split(" ")
            for word in words:
                if word in positive_feedback:
                    score += 3
                if word in negative_feedback:
                    score -= 1

            heapq.heappush(maxHeap, (-score, student_id[i]))

        res = []

        for _ in range(k):
            _, top = heapq.heappop(maxHeap)
            res.append(top)

        return res
                