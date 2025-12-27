class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.capacity = [big, medium, small]

    def addCar(self, carType: int) -> bool:
        ndx = carType - 1
        if not self.capacity[ndx]:
            return False

        self.capacity[ndx] -= 1
        return True
