# Standard imports
import sys
import pathlib
import json
from datetime import datetime
import logging
import logging.config

# Custom imports
from app.calculator import add, subtract


if __name__ == "__main__":
    # Get current datetime, format for logger filename.
    log_datetime = datetime.now().strftime("%Y%m%d_%H%M%S")

    # Create logs folder, if it doesn't already exist.
    log_path = pathlib.Path("../logs")
    if not log_path.exists():
        log_path.mkdir(parents=True, exist_ok=True)

    # Create custom logger.
    logger = logging.getLogger("my_app")

    # Load custom logging config from json file.
    config_file = pathlib.Path("src/logging_config.json")
    with open(config_file) as file:
        logging_config = json.load(file)
    logging_config["handlers"]["file"]["filename"] = f"../logs/app-{log_datetime}.log"

    # configure root logger with custom config.
    logging.config.dictConfig(config=logging_config)

    # Use application.
    x, y = 1, 2

    logger.info("Performing 1+2...")
    ans1 = add(x, y)
    logger.info(f"Answer is {ans1}")

    logger.info("Performing 1-2...")
    ans2 = subtract(x, y)
    logger.info(f"Answer is {ans2}")
