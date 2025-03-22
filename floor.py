import random
import building
import room


class Floor:
    def __init__(self):
        self.prev_floor: Floor = None
        self.next_floor: Floor = None
        self.floor_number: int = None
        self.rooms: list["room.Room"] = []
        self.building: "building.Building" = None

    def getRandomRoom(self) -> "room.Room":
        return random.choice(self.rooms)

    def setBuilding(self, building: "building.Building"):
        self.building = building

    def addPrevFloor(self, floor: "Floor"):
        self.prev_floor = floor

    def addNextFloor(self, floor: "Floor"):
        self.next_floor = floor

    def addRoom(self, room: "room.Room"):
        if len(self.rooms) != 0:
            prevRoom = self.rooms[-1]
            prevRoom.addNextRoom(room)
            room.addPrevRoom(prevRoom)
        self.rooms.append(room)
        room.setFloor(self)
        room.setFloorNumber(len(self.rooms)-1)

    def setFloorNumber(self, floor_number: int):
        self.floor_number = floor_number

    def getRoom(self, room_number: int) -> "room.Room":
        return self.rooms[room_number]

    def hasNextFloor(self):
        return self.next_floor is not None

    def hasPrevFloor(self):
        return self.prev_floor is not None
