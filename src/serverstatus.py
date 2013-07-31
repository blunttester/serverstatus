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

pid = str(os.getpid())
pidfile = "/tmp/serverstatus.pid"

if os.path.isfile(pidfile):
    print "%s already exists, exiting" % pidfile
    print "Consider removing the file manually"
    print "It seems that the application has crashed unexpected previously and not cleaned itself (TODO)"
    sys.exit()
else:
    file(pidfile, 'w').write(pid)

# Do some actual work here
myTop = srvstat.top()
myOutput = iostream.writeStream(myTop, fname)
myInput = iostream.readStreamFromFile(fname)
myStream = iostream.sendStream(myTop, 'localhost', 7878)
print str(myTop)
print str(myInput).split()

time.sleep(10)

os.unlink(pidfile)