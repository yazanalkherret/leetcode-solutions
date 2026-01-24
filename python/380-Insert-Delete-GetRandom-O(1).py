class RandomizedSet:

    def __init__(self):
        self.elements = []
        self.indices_map = {}

    def insert(self, val: int) -> bool:
        if val in self.indices_map: return False

        self.indices_map[val] = len(self.elements)
        self.elements.append(val) 
        return True

    def remove(self, val: int) -> bool:
        if val not in self.indices_map: return False

        last_element = self.elements[-1]
        cur_index = self.indices_map[val]

        self.elements[cur_index] = last_element
        self.indices_map[last_element] = cur_index
        self.elements.pop()

        del self.indices_map[val]

        return True

    def getRandom(self) -> int:
        random_index = randint(0, len(self.elements) - 1) 
        return self.elements[random_index]
