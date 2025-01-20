import gzip
import logging
import os
import sys
from logging.handlers import TimedRotatingFileHandler


def rotate_log(source, dest):
    os.rename(source, dest)
    with open(dest, 'rb') as f_in:
        compressed_data = gzip.compress(f_in.read())
    with open(dest + '.gz', 'wb') as f_out:
        f_out.write(compressed_data)


def _reset_logger(log):
    for handler in log.handlers:
        handler.close()
        log.removeHandler(handler)
        del handler
    log.handlers.clear()
    log.propagate = False
    console_handle = logging.StreamHandler(sys.stdout)
    console_handle.setFormatter(
        logging.Formatter(
            "[%(levelname)s][%(asctime)s][%(filename)s:%(lineno)d] - %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S",
        )
    )
    # Use TimedRotatingFileHandler for daily log rotation
    file_handle = TimedRotatingFileHandler("logs/run.log", when="midnight", interval=1, backupCount=7, encoding="utf-8")
    file_handle.setFormatter(
        logging.Formatter(
            "[%(levelname)s][%(asctime)s][%(filename)s:%(lineno)d] - %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S",
        )
    )
    file_handle.namer = lambda name: name + ".gz"
    file_handle.rotator = rotate_log
    log.addHandler(file_handle)
    log.addHandler(console_handle)


def _get_logger():
    log = logging.getLogger("log")
    _reset_logger(log)
    log.setLevel(logging.INFO)
    return log


# 日志句柄
logger = _get_logger()
