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

        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)

        self.logger.addHandler(console_handler)