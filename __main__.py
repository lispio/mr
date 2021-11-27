#!/opt/lispio/mr/mrSvr_venv/bin/python
import sys

from twisted.web import server, resource
from twisted.internet import reactor, endpoints

from src.mrSvr import Simple


def main():
    print("mrSvr started")
    site = server.Site(Simple())
    endpoint = endpoints.TCP4ServerEndpoint(reactor, 8078)
    endpoint.listen(site)
    reactor.run()


if __name__ == '__main__':
    sys.exit(main())
