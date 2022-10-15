import logging


class Problem:
    def __init__(self, description):
        self.description = description
        logging.debug(f'Problem Created {self.description}')