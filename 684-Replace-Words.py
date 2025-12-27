# Time Complexity: O(d * w + s * w)
# Space Complexity: O(d * w + s * w)

class TrieNode:
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.is_dictionary_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word) -> None:
        curr = self.root
        for c in word:
            curr = curr.children[c]
        curr.is_dictionary_word = True

    def shortest_prefix(self, word) -> str:
        curr = self.root

        for i, c in enumerate(word):

            if curr.is_dictionary_word:
                return word[:i]
            
            if c not in curr.children:
                return word

            curr = curr.children[c]

        return word

class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        words = sentence.split()
        trie = Trie()

        for dictionary_word in dictionary:
            trie.insert(dictionary_word)

        res = []
        for word in words:
            res.append(trie.shortest_prefix(word))

        return " ".join(res)
