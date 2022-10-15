SCENARIO_TYPE_CHOICES = (
    'phone_call'
)


class Scenario:
    def __init__(self, type):
        if type in SCENARIO_TYPE_CHOICES:
            self.type = type
        else:
            raise
