import floor


class Building:
    def __init__(self):
        self.floors: list["floor.Floor"] = []

    def addFloor(self, floor: "floor.Floor"):
        self.floors.append(floor)
        floor.setFloorNumber(len(self.floors)-1)
        floor.setBuilding(self)

    def getFloor(self, number: int) -> "floor.Floor":
        return self.floors[number]
    
    def getFirstFloor(self) -> "floor.Floor":
        return self.getFloor(0)
