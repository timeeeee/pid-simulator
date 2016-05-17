from blackbox import FactorBlackbox
from controller import PIController
from view import PrintView
from simulation import simulate


if __name__ == "__main__":
    blackbox = FactorBlackbox(.5)
    controller = PIController(1, 1, 10)
    view = PrintView()

    simulate(blackbox, controller, view)
