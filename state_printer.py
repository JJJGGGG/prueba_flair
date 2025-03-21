import sensor
from colorama import Fore
from colorama import Style

class StatePrinter:
    def __init__(self, n_floors: int, n_rooms: int):
        self.sensors: list["sensor.Sensor"] = []
        self.floors = n_floors
        self.rooms = n_rooms

    def setSensors(self, sensors: list["sensor.Sensor"]):
        self.sensors = sensors
        for sens in self.sensors:
            sens.addObserver(self)

    def printState(self):
        print("Sensor map:")
        print("     -" + "----" * self.rooms)
        for floor in range(self.floors):
            print(f"{floor+1: ^5d}|", end="")
            for room in range(self.rooms):
                sens = self.getSensor(floor, room)
                print(f" {self.getSensorState(sens)} |", end="")
            print()
            print("     -" + "----" * self.rooms)

    def triggerExitZombie(self, sensor: "sensor.Sensor"):
        print(f"All zombies have left room {sensor.room_number} in floor {sensor.floor_number}")

    def triggerEnterZombie(self, sensor: "sensor.Sensor"):
        print(f"Zombies have entered room {sensor.room_number} in floor {sensor.floor_number}")

    def getSensor(self, floor: int, room: int):
        return next(s for s in self.sensors if s.floor_number == floor and s.room_number == room)
    
    def getSensorState(self, sens: "sensor.Sensor"):
        if sens.state == sensor.SensorStates.NORMAL:
            return " "
        elif sens.state == sensor.SensorStates.ALERT:
            return f"{Fore.RED}!{Style.RESET_ALL}"


"""
-------------------------------
|     |     |     |     |     |
-------------------------------
|     |     |     |     |     |
-------------------------------
"""
