import sys
import copy
import logging
import inspect


class InfoFilter(logging.Filter):
    def filter(self, record):
        return record.levelno == logging.INFO


class MyLogger:
    def __init__(self, name):
        self.logger = logging.getLogger(name)
        self.logger.setLevel(logging.DEBUG)

        formatter = logging.Formatter(
            "%(asctime)s - %(levelname)s - %(name)s - %(funcName)s  - line:%(lineno)d - %(message)s"
        )

        log_file_path = "log/debug.log"
        file_handler = logging.FileHandler(filename=log_file_path, encoding="utf-8")
        file_handler.setLevel(logging.DEBUG)
        file_handler.setFormatter(formatter)

        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.setLevel(logging.INFO)
        console_handler.setFormatter(formatter)
        info_filter = InfoFilter()
        console_handler.addFilter(info_filter)

        warning_handler = logging.StreamHandler(sys.stderr)
        warning_handler.setLevel(logging.WARNING)
        warning_handler.setFormatter(formatter)

        self.logger.addHandler(file_handler)
        self.logger.addHandler(console_handler)
        self.logger.addHandler(warning_handler)


def get_params_function(frame):
    args, _, _, values = inspect.getargvalues(frame)
    tmp_result1 = {}
    tmp_result2 = {}
    for i in args:
        if isinstance(values[i], (list, dict, str)):
            tmp_result1[i] = values[i]
        else:
            tmp_result2[i] = values[i]
    export_result = copy.deepcopy(tmp_result1)
    if tmp_result2:
        export_result.update(tmp_result2)
    return export_result