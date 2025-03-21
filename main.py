from __future__ import annotations
from menu import MainMenu
from simulation import Simulation
import colorama

def main():

    m = MainMenu
    while True:
        m = m.printOptions()

    simulation = Simulation()
    simulation.setupSimulation(3, 4, 5)

    simulation.simulation_step()

    simulation.printState()


if __name__ == "__main__":
    colorama.init()
    main()
