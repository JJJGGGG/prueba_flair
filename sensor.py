from enum import Enum


class SensorStates(Enum):
    NORMAL = "normal"
    ALERT = "alert"


class Sensor:
    def __init__(self, floor_number, room_number):
        self.state = SensorStates.NORMAL
        self.floor_number = floor_number
        self.room_number = room_number
        self.observers = []

    def addObserver(self, observer):
        self.observers.append(observer)

    def triggerSensor(self):
        if self.state != SensorStates.ALERT:
            self.state = SensorStates.ALERT
            for observer in self.observers:
                observer.triggerEnterZombie(self)

    def resetSensor(self):
        if self.state != SensorStates.NORMAL:
            self.state = SensorStates.NORMAL
            for observer in self.observers:
                observer.triggerExitZombie(self)
