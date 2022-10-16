from .scenario import PhoneCallScenario
from .exceptions import BoatLoanBotException


class BoatLoanBot:
    def __init__(self, name='Boat Loan Bot'):
        self.name = name
        self.scenario = None

    def start_scenario(self, type):
        if type == 'phone_call':
            self.scenario = PhoneCallScenario(self)
            self.scenario.start()
            self.scenario.evaluate()
        else:
            raise BoatLoanBotException(f'"{type}" is not valid choice')

    def end_scenario(self):
        self.scenario.end()

    def run_scenario(self):
        pass
