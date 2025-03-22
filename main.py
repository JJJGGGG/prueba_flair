from __future__ import annotations
from menu import MainMenu
from simulation import Simulation
import colorama

def main():

    m = MainMenu
    simulation = Simulation()
    while True:
        m = m.printOptions(simulation)


if __name__ == "__main__":
    colorama.init()
    main()
