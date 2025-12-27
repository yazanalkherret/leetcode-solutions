class Encrypter:

    def __init__(self, keys: List[str], values: List[str], dictionary: List[str]):
        self.encryptMap = { k : v for k, v in zip(keys, values) }
        self.possibleDecrypt = defaultdict(int)

        for word in dictionary:
            self.possibleDecrypt[self.encrypt(word)] += 1

    def encrypt(self, word1: str) -> str:
        encrypted = []
        for char in word1:
            if char not in self.encryptMap:
                return ""
            
            encrypted.append(self.encryptMap[char])

        return "".join(encrypted)

    def decrypt(self, word2: str) -> int:
        return self.possibleDecrypt[word2]
