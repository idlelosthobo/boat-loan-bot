import logging

from boat_loan_bot import blb

logging.basicConfig(
    format='%(asctime)s [%(levelname)s] %(name)s: "%(message)s"',
    datefmt='%m/%d/%Y %I:%M:%S %p',
    # filename='boat_loan_bot.log',
    encoding='utf-8',
    level=logging.DEBUG
)

blb.start_scenario('phone_call')

TEST_CONVERSATION_LINES = (
    'This is Bob Smith calling about the horse you had for sale.',
)

for line in TEST_CONVERSATION_LINES:
    blb.scenario.string_input(line)
