#/usr/bin/env python
'''
Created on 31.7.2013

@author: janmatilainen
'''

if __name__ == '__main__':
    pass


import os
import sys
import time

from pySrvStats import *
from pyIoStream import *
fname = "./tmpfile"
srvstat = SrvStats()
iostream = IoStream()

cfgFolder = '../conf/'
cfgFile = cfgFolder+'conf.conf'
appname = ''
f = open(cfgFile,'r')
for line in f:
    confline = line.split(':')
    if confline[0] == 'appname':
        appname = confline[1].split('\n')[0] #Linefeed caused a lot of unnecessary editing !!!
f.close()

pid = str(os.getpid())
pidfile = "/tmp/serverstatus.pid"

if os.path.isfile(pidfile):
    print "%s already exists, exiting" % pidfile
    print "Consider removing the file manually"
    print "It seems that the application has crashed unexpected previously and not cleaned itself (TODO)"
    myConfirm = raw_input('Removing the %s automatically? Press Y to confirm, N to exit: ( Y/N )' % pidfile) 
    if myConfirm.lower() == 'n':
        print "Goodbye!"
        sys.exit()
    else:
        file(pidfile, 'w+').write(pid)
else:
    file(pidfile, 'w').write(pid)

# Do some actual work here
myTop = srvstat.top()
myCpu = srvstat.cpu(appname)
myOutput = iostream.writeStream(myTop, fname)
myInput = iostream.readStreamFromFile(fname)
#myStoreTop = iostream.writeStreamToSqlite(myTop)
myAppMem = srvstat.mem(appname)
myThreads = srvstat.threads(appname)
#myStream = iostream.sendStream(myCpu, 'localhost', 7878)
#myStream = iostream.sendStream(myTop, 'localhost', 7878)
#print str(myTop)
#print str(myInput).split()
print appname + ' CPU: ' + str(myCpu) + ' MEM: ' + str(myAppMem) + ' Threads: ' + str(myThreads)


time.sleep(10)

os.unlink(pidfile)