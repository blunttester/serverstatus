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



def createTable(myTop):

    cols = []
    myRow = []
    
    for x in xrange(len(myTop)):
        
       
        myRow.append(myTop[x].split())
        cols.append('<tr>')
        for y in xrange(len(myRow[0])):            
            if len(myRow[x]) >= len(myRow[0]):                
                cols.append('<th>' +  myRow[x][y] + '</th>')
         

        cols.append('</tr>')
        myTable = ''.join(str(cols).split(',')).replace('\'','').replace('[','').replace(']','')
        myTable = '<tr>' + myTable + '</tr>'
        
    return myTable
class ClockPage(Resource):
    isLeaf = True
    def render_GET(self, request):
        srvstats = SrvStats()
        myTable = createTable(srvstats.top())
        return "<html><body><p>%s<p><table>%s</table></body></html>" % (time.ctime(),str(myTable))

resource = ClockPage()
factory = Site(resource)
reactor.listenTCP(8780, factory)
reactor.run()