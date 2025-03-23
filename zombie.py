import random
import room
from faker import Faker

fake = Faker()


class Zombie:
    def __init__(self, name: str):
        self.name = name
        self.room: "room.Room" = None

    def moveToRoom(self, newRoom: "room.Room"):
        if self.room is not None:
            self.room.exitZombie(self)
        newRoom.enterZombie(self)
        self.room = newRoom

    def moveToNextRoom(self):
        if self.room.hasNextRoom():
            newRoom = self.room.nextRoom
            self.moveToRoom(newRoom)

    def moveToPreviousRoom(self):
        if self.room.hasPrevRoom():
            newRoom = self.room.prevRoom
            self.moveToRoom(newRoom)

    def moveToUpRoom(self):
        if self.room.floor.hasNextFloor():
            newRoom = self.room.floor.next_floor.getRoom(self.room.room_number)
            self.moveToRoom(newRoom)

    def moveToDownRoom(self):
        if self.room.floor.hasPrevFloor():
            newRoom = self.room.floor.prev_floor.getRoom(self.room.room_number)
            self.moveToRoom(newRoom)

    def stayInRoom(self):
        pass

    @staticmethod
    def createRandomName():
        return fake.name()
