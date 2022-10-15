from .scenario import Scenario


class BoatLoanBot:
    def __init__(self):
        self._scenario = None

    def set_scenario(self, type):
        self._scenario = Scenario(type)


blb = BoatLoanBot()
