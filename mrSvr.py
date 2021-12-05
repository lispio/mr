#!/opt/lispio/mr/mrSvr_venv/bin/python
import sys
import time
import logging
import logging.handlers as handlers
import uvicorn
from fastapi import FastAPI

from src.endpoints import app

log = logging.getLogger('mrSvr')
log.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s %(levelname)s %(module)s %(funcName)s %(lineno)d: %(message)s')
logHandler = handlers.TimedRotatingFileHandler('logs/mrSvr.log',  interval=1, delay=False, backupCount=0)
logHandler.setLevel(logging.DEBUG)
logHandler.setFormatter(formatter)
log.addHandler(logHandler)


if __name__ == "__main__":
    log.info("server Start")
    uvicorn.run(app, host="127.0.0.1", port=7979)
    log.info("server stops")
