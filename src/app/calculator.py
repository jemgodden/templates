from typing import Any
import logging


# Set application logger.
logging.getLogger('app.calculator').addHandler(logging.NullHandler())


def check_input_type(value: Any, input_type: type) -> None:
    if type(value) != input_type:
        logging.error("Input is not required type.")
        raise TypeError("Input is not an integer.")


def add(x: int, y: int) -> int:
    logging.info("Using 'add' function.")

    logging.info("Checking input types...")
    check_input_type(x, int)
    check_input_type(y, int)
    logging.info("Input types valid.")

    return x + y


def subtract(x: int, y: int) -> int:
    logging.info("Using 'subtract' function.")

    logging.info("Checking input types...")
    check_input_type(x, int)
    check_input_type(y, int)
    logging.info("Input types valid.")

    return x - y
