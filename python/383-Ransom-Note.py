# Time Complexity: O(n)
# Space Complexity: O(n)

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        count_note = Counter(ransomNote)
        count_magazine = Counter(magazine)

        for letter, freq in count_note.items():
            if freq > count_magazine[letter]:
                return False


        return True
