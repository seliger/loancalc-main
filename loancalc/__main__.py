import logging
import atexit
import sys

import loancalc
from loancalc.controller import LoanCalc

logger = logging.getLogger(__name__)

# Helper function to ensure we capture stack traces via logging
# (Note: This method does not work with threads until Python 3.8)
def log_excepthook (excType, excValue, traceback, logger=logging.getLogger(__name__)):
    logger.error("Logging an uncaught exception",
                  exc_info=(excType, excValue, traceback))


# Helper function to clean up and alert that we are ending runtime
@atexit.register
def shutdown():
    logger.info(f"{loancalc.APP_NAME} {loancalc.APP_VERSION} - Shutting down...")


# Stub code to bootstrap environment and launch into main application
def run():
    # Configure logging
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(name)s] [%(funcName)s] [%(levelname)s]  %(message)s",
        handlers=[
            logging.StreamHandler(sys.stderr),
            logging.FileHandler("{0}/{1}.log".format("./", loancalc.APP_EXE_NAME.lower()))
        ]
    )
    logger = logging.getLogger(__name__)

    # Ensure we capture stack traces in our log
    sys.excepthook = log_excepthook

    # Announce that we are starting up.
    logger.info(f'{loancalc.APP_NAME} {loancalc.APP_VERSION} - Starting up...')

    # Launch into the main application run code
    LoanCalc.run()


if __name__ == '__main__':
    run()
