import sys
import logging


class MyLogger:
    def __init__(self, name):
        self.logger = logging.getLogger(name)
        self.logger.setLevel(logging.DEBUG)

        formatter = logging.Formatter(
            "%(asctime)s - %(name)s - %(funcName)s - %(levelname)s - line:%(lineno)d - %(message)s"
        )

        # file_handler = logging.FileHandler(filename)
        # file_handler.setFormatter(formatter)
        # self.logger.addHandler(file_handler)

        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.setLevel(logging.DEBUG)
        console_handler.setFormatter(formatter)

        error_handler = logging.StreamHandler(sys.stderr)
        error_handler.setLevel(logging.WARNING)
        error_handler.setFormatter(formatter)


        self.logger.addHandler(console_handler)
        self.logger.addHandler(error_handler)