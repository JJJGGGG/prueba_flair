import floor
import sensor
import zombie


class Room:
    def __init__(self):
        self.sensor: "sensor.Sensor" = None
        self.zombies: list["zombie.Zombie"] = []
        self.prevRoom: Room = None
        self.nextRoom: Room = None
        self.floor: "floor.Floor" = None
        self.room_number = None

    def setFloor(self, floor: "floor.Floor"):
        self.floor = floor

    def setFloorNumber(self, n: int):
        self.room_number = n

    def addSensor(self, sensor: "sensor.Sensor"):
        self.sensor = sensor

    def addPrevRoom(self, room: "Room"):
        self.prevRoom = room

    def addNextRoom(self, room: "Room"):
        self.nextRoom = room

    def hasPrevRoom(self):
        return self.prevRoom is not None

    def hasNextRoom(self):
        return self.nextRoom is not None

    def hasNoZombies(self):
        return len(self.zombies) == 0

    def exitZombie(self, zombie: "zombie.Zombie"):
        self.zombies.remove(zombie)
        # if self.hasNoZombies():
        #     self.sensor.resetSensor()

    def enterZombie(self, zombie: "zombie.Zombie"):
        self.sensor.triggerSensor()
        self.zombies.append(zombie)
