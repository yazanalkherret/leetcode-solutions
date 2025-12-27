# Not a very elegant solution

class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        freq = Counter(s)
        repeat = defaultdict(int)

        inHeap = set((-ord(c), c) for c in s)
        maxHeap = list(inHeap)
        heapq.heapify(maxHeap)

        prev = None
        res = ""
        while maxHeap:
            _, char = heapq.heappop(maxHeap)
            repeat[char] += 1
            res += char
            freq[char] -= 1
            inHeap.discard((-ord(char), char))

            if prev and prev != char:
                repeat[prev] = 0

            if prev and prev != char and freq[prev] > 0 and (-ord(prev), prev) not in inHeap:
                heapq.heappush(maxHeap, (-ord(prev), prev))
                inHeap.add((-ord(prev), prev))

            if repeat[char] != repeatLimit and freq[char] > 0:
                heapq.heappush(maxHeap, (-ord(char), char))
                inHeap.add((-ord(char), char))

            prev = char


        return res