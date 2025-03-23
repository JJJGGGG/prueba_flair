import random
import typing

import simulation
import os


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def input_int(message: str, min: int, max: int):
    i = None
    while i is None:
        try:
            i = int(input(message))
        except (ValueError):
            clear_screen()
            print("The value entered is not an integer")
        if i < min or i > max:
            i = None
            clear_screen()
            print(f"The value entered is not between {min} and {max}")
    return i


class Menu:
    options: list[tuple[str, typing.Callable[["simulation.Simulation"], "Menu"]]] = []
    @classmethod
    def promptOptionSelection(cls):
        option = None
        while option is None:
            try:
                i = int(input("Select an option: "))
                option = cls.options[i-1]
            except (ValueError, IndexError):
                print("Option incorrect, please try again")
        return option

    @classmethod
    def printOptions(cls, sim):
        clear_screen()
        print(cls.menu_name)
        for i, (option, _) in enumerate(cls.options):
            print(f"{i+1: >3d}: {option}")

        name, action = cls.promptOptionSelection()

        clear_screen()

        newMenu = action(sim)

        return newMenu

class TurnMenu(Menu):
    menu_name = "Simulation Menu"
    options = [
        ("Advance Simulation", lambda sim: TurnMenu.advanceSimulation(sim)),
        ("Show Current State", lambda sim: TurnMenu.showCurrentState(sim)),
        ("End Simulation", lambda sim: MainMenu)
    ]

    @staticmethod
    def advanceSimulation(sim: "simulation.Simulation"):
        print("Sensor Messages this turn:")
        sim.simulation_step()
        input()
        return TurnMenu

    @staticmethod
    def showCurrentState(sim: "simulation.Simulation"):
        sim.printState()
        input()
        return TurnMenu

class MainMenu(Menu):
    menu_name = "Main Menu"
    options = [
        ("Start Simulation", lambda sim: MainMenu.selectParameters(sim)),
        ("Exit", lambda sim: MainMenu.exit())
    ]

    @staticmethod
    def selectParameters(simulation: "simulation.Simulation"):
        floors_count = input_int("Enter the number of floors of the building (max 11): ", 1, 11)
        rooms_per_floor = input_int("Enter the number of rooms per floor (max 8): ", 1, 8)

        simulation.setupBuilding(floors_count, rooms_per_floor)
        zombieCount = random.randint(1, 20)

        clear_screen()

        simulation.addZombies(zombieCount)

        input()

        return TurnMenu

    @staticmethod
    def exit():
        print("Exiting...")
        exit(0)
