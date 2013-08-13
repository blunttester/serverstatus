#!/usr/bin/python
#'''
#Created on Aug 5, 2013
#
#@author: janmatilainen
#'''

if __name__ == '__main__':
    pass

from twisted.internet import reactor
from twisted.web.server import Site
from twisted.web.resource import Resource
from pySrvStats import *
import time
import json

cfgFolder = '../conf/'
cfgFile = cfgFolder+'conf.conf'
appname = ''
f = open(cfgFile,'r')
for line in f:
	confline = line.split(':')
	if confline[0] == 'appname':
		appname = str(confline[1]).split('\n')[0]
f.close()
	

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


class TablePage(Resource):
    isLeaf = True
    def render_GET(self, request):
        srvstats = SrvStats()
        myTable = createTable(srvstats.top())
	myAppTable = srvstats.appTop(appname).split()
	aTable = []
	aTable.append('<tr>')
	for x in range(len(myAppTable)):
		aTable.append('<th>' + myAppTable[x] + '</th>')
	aTable.append('</tr>')
	myATable = ''.join(str(aTable).split(',')).replace('\'','').replace('[','').replace(']','')	
        return "<html><body><p>%s<p><table>%s</table><table>%s</table></body></html>" % (time.ctime(),str(myTable),str(myATable))

class JsonPage(Resource):

    isLeaf = True
    def render_GET(self, request):
        srvstats = SrvStats()
	myAppInfo = srvstats.appTop(appname)
	#print myAppInfo
	myString = 'u\"{ tstamp : \"%s\" , tdata : \"%s\" }\"' % (time.ctime(),str(myAppInfo))
	#print myString
	json_string = json.dumps(myString)
	obj = json.loads(json_string)
	#print obj
	return str(obj)

class StatusPage(Resource):

    isLeaf = True
    def render_GET(self, request):
        srvstat = SrvStats()
        myCpu = srvstat.cpu(appname)
        myAppMem = srvstat.mem(appname)
        myThreads = srvstat.threads(appname)
        obj1 = 'Application: ' + appname + ' CPU: ' + str(myCpu) + ' MEM: ' + str(myAppMem) + ' Threads: ' + str(myThreads)
        return  obj1

resource = TablePage()
res2 = JsonPage()
res3 = StatusPage()
factory = Site(resource)
factory2 = Site(res2)
factory3 = Site(res3)
reactor.listenTCP(8780, factory)
reactor.listenTCP(8788, factory2)
reactor.listenTCP(8789, factory3)
reactor.run()
