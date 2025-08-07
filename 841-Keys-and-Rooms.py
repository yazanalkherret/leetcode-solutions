class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        keys = set() # Maintain a set of all visited rooms (keys in posession)

        def dfs(ndx, keys):
            # Base condition is unnecessary 
            # if there is a conditional inside the for loop
            keys.add(ndx)
            for key in rooms[ndx]:
                if key not in keys:
                    dfs(key, keys)

        dfs(0, keys)
        return len(keys) == len(rooms)


        