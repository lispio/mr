#!/opt/lispio/mr/mrSvr_venv/bin/python
import sys
import time
import logging
import logging.handlers as handlers

from twisted.web import server, resource
from twisted.internet import reactor, endpoints

from src.mrSvr import MrSvrEndpoints
from src.templates.mrSvrTemplates import MrSvr

log = logging.getLogger('mrSvr')
log.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s %(levelname)s %(module)s %(funcName)s %(lineno)d: %(message)s')
logHandler = handlers.TimedRotatingFileHandler('logs/mrSvr.log',  interval=1, delay=False, backupCount=0)
logHandler.setLevel(logging.DEBUG)
logHandler.setFormatter(formatter)
log.addHandler(logHandler)


def main():
    log.info(f"rmSvr start on port: {MrSvr.port.value}")
    site = server.Site(MrSvrEndpoints())
    endpoint = endpoints.TCP4ServerEndpoint(reactor, MrSvr.port.value)
    endpoint.listen(site)
    reactor.run()


if __name__ == '__main__':
    sys.exit(main())
