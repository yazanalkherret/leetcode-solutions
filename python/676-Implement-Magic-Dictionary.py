class MagicDictionary:

    def __init__(self):
        self.accepted_strings = defaultdict(int)
        self.dictionary_words = set()

    # Time Complexity: O(m * n^2)
    def buildDict(self, dictionary: List[str]) -> None:
        for word in dictionary:
            self.dictionary_words.add(word)
            for i in range(len(word)):
                starred = word[:i] + '*' + word[i + 1:]
                self.accepted_strings[starred] += 1

    # Time Complexity: O(k^2)
    def search(self, searchWord: str) -> bool:

        for i in range(len(searchWord)):
            starred = searchWord[:i] + '*' + searchWord[i + 1:]
            if (
                starred in self.accepted_strings
                and (
                    self.accepted_strings[starred] > 1
                    or searchWord not in self.dictionary_words
                )):
                return True
                
        return False
