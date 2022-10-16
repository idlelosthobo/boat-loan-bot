import logging

from .problem import Problem


class Scenario:
    def __init__(self, boat_loan_bot):
        self.actor_list = list()
        self.problem_list = list()
        self.boat_loan_bot = boat_loan_bot

    def start(self):
        pass

    def end(self):
        pass

    def evaluate(self):
        for actor in self.actor_list:
            if actor.is_known == False:
                self.problem_list.append(Problem(f'An actor is unknown.'))

    def string_input(self, string):
        logging.debug(f'')


class PhoneCallScenario(Scenario):
    def start(self):
        logging.debug('Phone Call Scenario: Started')
        from .actor import CallerActor, ReceptionActor
        self.actor_list.append(ReceptionActor(is_bot=True, is_known=True, name=self.boat_loan_bot.name))
        self.actor_list.append(CallerActor(is_bot=False, is_known=False))