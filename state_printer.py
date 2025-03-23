import building
import sensor
from colorama import Fore
from colorama import Style


class StatePrinter:
    def __init__(self, building: "building.Building", n_floors: int, n_rooms: int):
        self.sensors: list["sensor.Sensor"] = []
        self.floors = n_floors
        self.rooms = n_rooms
        self.building = building

    def setSensors(self, sensors: list["sensor.Sensor"]):
        self.sensors = sensors
        for sens in self.sensors:
            sens.addObserver(self)

    def printState(self):
        print(f"{'F':^5s}Sensor map:" + " " * (self.rooms * 4 - 10) + "     Zombies Map:")
        print("     -" + "----" * self.rooms + "     -" + "----" * self.rooms)
        for floor in range(self.floors-1, -1, -1):
            print(f"{floor+1: ^5d}|", end="")
            for room in range(self.rooms):
                sens = self.getSensor(floor, room)
                print(f" {self.getSensorState(sens)} |", end="")
            print("     |", end="")
            for room in range(self.rooms):
                rroom = self.building.getFloor(floor).getRoom(room)
                print(f"{len(rroom.zombies):^3d}|", end="")
            print()
            print("     -" + "----" * self.rooms + "     -" + "----" * self.rooms)

    def triggerExitZombie(self, sensor: "sensor.Sensor"):
        print(f"All zombies have left room {sensor.room_number+1} in floor {sensor.floor_number+1}")

    def triggerEnterZombie(self, sensor: "sensor.Sensor"):
        print(f"Zombies have entered room {sensor.room_number+1} in floor {sensor.floor_number+1}")

    def getSensor(self, floor: int, room: int):
        return next(s for s in self.sensors if s.floor_number == floor and s.room_number == room)

    def getSensorState(self, sens: "sensor.Sensor"):
        if sens.state == sensor.SensorStates.NORMAL:
            return " "
        elif sens.state == sensor.SensorStates.ALERT:
            return f"{Fore.RED}!{Style.RESET_ALL}"
