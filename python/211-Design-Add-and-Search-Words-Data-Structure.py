class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEndOfWord = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root

        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.isEndOfWord = True

    def search(self, word: str) -> bool:
        
        def helper(curr, i, word):
            if i == len(word): return curr.isEndOfWord
            char = word[i]
            if char != '.' and char not in curr.children:
                return False

            if char == '.':
                res = False
                for child in curr.children:
                    res = res or helper(curr.children[child], i + 1, word)
                return res
            else:
                return helper(curr.children[char], i + 1, word)
        
        return helper(self.root, 0, word)
