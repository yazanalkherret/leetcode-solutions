class Bitset:

    def __init__(self, size: int):
        self.size = size
        self.bits = [0] * size
        self.countSet = 0
        self.flipped = False

    def fix(self, idx: int) -> None:
        if self.flipped:
            self.__unfix(idx)
        else:
            self.__fix(idx)

    def unfix(self, idx: int) -> None:
        if self.flipped:
            self.__fix(idx)
        else:
            self.__unfix(idx)

    def flip(self) -> None:
        self.flipped = not self.flipped    

    def all(self) -> bool:
        return self.count() == self.size

    def one(self) -> bool:
        return self.count() > 0

    def count(self) -> int:
        if self.flipped:
            return self.size - self.countSet
        return self.countSet

    def toString(self) -> str:
        if self.flipped:
            return self.__toFlippedString()

        return "".join(str(bit) for bit in self.bits)

    def __toFlippedString(self):
        return "".join(["0" if bit else "1" for bit in self.bits])

    def __fix(self, idx: int) -> None:
        if self.bits[idx]: return

        self.bits[idx] = 1
        self.countSet += 1

    def __unfix(self, idx: int) -> None:
        if not self.bits[idx]: return

        self.bits[idx] = 0
        self.countSet -= 1
