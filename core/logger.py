import logging
from logging.handlers import RotatingFileHandler
import os


def setup_logger(app):
    log_level = logging.INFO

    formatter = logging.Formatter(
        "[%(asctime)s] [%(levelname)s] [%(name)s] %(message)s"
    )

    log_dir = "logs"
    os.makedirs(log_dir, exist_ok=True)

    file_handler = RotatingFileHandler(
        os.path.join(log_dir, "app.log"),
        maxBytes=1_000_000,
        backupCount=3
    )
    file_handler.setFormatter(formatter)
    file_handler.setLevel(log_level)

    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    console_handler.setLevel(log_level)

    app.logger.setLevel(log_level)
    app.logger.addHandler(file_handler)
    app.logger.addHandler(console_handler)

    return app.logger