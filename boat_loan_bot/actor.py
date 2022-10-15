class Actor:
    def __init__(
            self,
            is_bot=False,
            is_known=False,
            name=None
    ):
        self.is_bot = is_bot
        self.is_known = is_known
        self.name = name


class CallerActor(Actor):
    pass


class ReceptionActor(Actor):
    pass