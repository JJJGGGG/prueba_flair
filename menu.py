import typing

import simulation

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
    def printOptions(cls):
        print(cls.__name__)
        for i, (option, _) in enumerate(cls.options):
            print(f"{i+1: >3d}: {option}")

        name, action = cls.promptOptionSelection()

        newMenu = action()

        return newMenu

class SelectionMenu(Menu):
    options = [
        ("Stay", lambda sim: SelectionMenu),
        ("Back", lambda sim: MainMenu)
    ]

class MainMenu(Menu):
    options = [
        ("Start Simulation", lambda sim: SelectionMenu),
        ("Print Something", lambda sim: MainMenu.printSomething())
    ]
    @classmethod
    def printSomething(self):
        print("Hola")
        return MainMenu

