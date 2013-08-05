'''
Created on Aug 5, 2013

@author: janmatilainen
'''

if __name__ == '__main__':
    pass

from twisted.internet import reactor
from twisted.web.server import Site
from twisted.web.resource import Resource
from pySrvStats import *
import time

srvstats = SrvStats()
myTop = srvstats.top()

class ClockPage(Resource):
    isLeaf = True
    def render_GET(self, request):
        return "<html><body><p>%s<p>%s</body></html>" % (time.ctime(),str(myTop))

resource = ClockPage()
factory = Site(resource)
reactor.listenTCP(8880, factory)
reactor.run()