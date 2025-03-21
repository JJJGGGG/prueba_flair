import building
import floor
import room
import sensor


class Builder:
    def __init__(self):
        self.building = None

    def buildBuilding(self):
        self.building = building.Building()
        self.sensors: list["sensor.Sensor"] = []

    def buildFloor(self):
        new_floor = floor.Floor()
        self.building.addFloor(new_floor)
        return new_floor.floor_number

    def buildRoom(self, floor_number: int) -> int:
        newRoom = room.Room()
        floor = self.building.getFloor(floor_number)
        floor.addRoom(newRoom)
        return newRoom.room_number

    def buildSensor(self, floor_number: int, room_number: int):
        sens = sensor.Sensor(floor_number, room_number)
        floor = self.building.getFloor(floor_number)
        room = floor.getRoom(room_number)
        room.addSensor(sens)
        self.sensors.append(sens)

    def getBuilding(self):
        return self.building
    
    def getSensors(self):
        return self.sensors
