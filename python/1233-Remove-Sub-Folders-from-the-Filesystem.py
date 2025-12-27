# Using sorting
# Time: O(N * L * Log N)
# Space: O(N * L)
# Sort then loop through folders and ignore subfolders
class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        folder.sort()
        res = []
        curr = folder[0]
        for f in folder:
            # If it is not a sub-folder
            if not f.startswith(curr + '/'):
                res.append(f)
                curr = f
        return res

# Using Trie