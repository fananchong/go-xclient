#! python3

import logging
import logging.handlers

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)


def init(filename):
    fmt = logging.Formatter("%(asctime)s %(pathname)s %(filename)s %(funcName)s %(lineno)s \
      %(levelname)s - %(message)s", "%Y-%m-%d %H:%M:%S")
    fh = logging.handlers.TimedRotatingFileHandler(filename, 'D')
    fh.setFormatter(fmt)
    logger.addHandler(fh)
    ch = logging.StreamHandler()
    ch.setFormatter(fmt)
    logger.addHandler(ch)


debug = logger.debug
info = logger.info
warning = logger.warn
error = logger.error
critical = logger.critical
