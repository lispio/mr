#!/opt/lispio/mr/mrSvr_venv/bin/python
import sys
import logging

from twisted.web import server, resource
from twisted.internet import reactor, endpoints

from src.mrSvr import Simple
from src.templates import MrSvr
logging.basicConfig(filename="log/mrSvr.log",
                    format='%(asctime)s %(levelname)s %(module)s %(funcName)s %(lineno)d: %(message)s',
                    )


# Creating an object
log = logging.getLogger()

# Setting the threshold of logger to DEBUG
log.setLevel(logging.DEBUG)


def main():
    print("mrSvr started")
    # Test messages
    log.info(f"rmSvr start on port: {MrSvr.port.value}")
    site = server.Site(Simple())
    endpoint = endpoints.TCP4ServerEndpoint(reactor, MrSvr.port.value)
    endpoint.listen(site)
    reactor.run()


if __name__ == '__main__':
    sys.exit(main())
