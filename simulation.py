import random
import builders
import building
import state_printer
import zombie


class Simulation:
    def __init__(self):
        self.building: building.Building = None
        self.zombies: list[zombie.Zombie] = []
        self.state_printer: list[state_printer.StatePrinter] = None

    def create_building(self, builder: builders.Builder, n_floors: int, n_rooms: int):
        builder.buildBuilding()
        for _ in range(n_floors):
            floor_number = builder.buildFloor()
            for _ in range(n_rooms):
                room_number = builder.buildRoom(floor_number)
                builder.buildSensor(floor_number, room_number)
        self.building = builder.building
        self.state_printer = state_printer.StatePrinter(self.building, n_floors, n_rooms)
        self.state_printer.setSensors(builder.sensors)

    def addZombie(self):
        # Que los zombies se metan en habitaciones random del primer piso
        # hacer getFirstFloor y getRandomRoom
        zombieName = zombie.Zombie.createRandomName()
        zomb = zombie.Zombie(zombieName)
        floor = self.building.getFirstFloor()
        room = floor.getRandomRoom()
        zomb.moveToRoom(room)
        self.zombies.append(zomb)

    def addZombies(self, zombieNumber):
        for _ in range(zombieNumber):
            self.addZombie()

    def setupBuilding(self, n_floors: int, n_rooms: int):
        builder = builders.Builder()
        self.create_building(builder, n_floors, n_rooms)

    def simulation_step(self):
        for zomb in self.zombies:
            moveZombie = random.choice([
                zomb.moveToDownRoom,
                zomb.moveToUpRoom,
                zomb.moveToPreviousRoom,
                zomb.moveToNextRoom,
                zomb.stayInRoom
            ])

            moveZombie()

    def printState(self):
        self.state_printer.printState()
