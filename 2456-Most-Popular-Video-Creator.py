from heapq import heappush, heappop
class Solution:
    def mostPopularCreator(self, creators: List[str], ids: List[str], views: List[int]) -> List[List[str]]:
        
        maxViews = 0
        main = defaultdict(lambda: [0, []]) # Creator: (total views, videos[])
        totalViewMap = defaultdict(set)

        for i, creator in enumerate(creators):
            totalViewMap[main[creator][0]].discard(creator)

            main[creator][0] += views[i]
            heappush(main[creator][1], (-views[i], ids[i]))

            maxViews = max(maxViews, main[creator][0])

            totalViewMap[main[creator][0]].add(creator)

        mostPopularCreators = totalViewMap[maxViews]

        res = []

        for creator in mostPopularCreators:

            res.append([creator, heappop(main[creator][1])[1]])

        return res