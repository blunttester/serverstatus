'''
Created on 31.7.2013

@author: janmatilainen
'''

class IoStream(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        
    def writeStream(self,stream,fname):
        self.stream = stream
        self.fname = fname
        f = open(fname,'a+')
        f.write(str(self.stream))
        f.close()
        
    def sendStream(self,stream,srv,port):
        import socket
        self.stream = stream
        self.srv = srv
        self.port = port

        s = socket.socket()
        s.connect((str(self.srv), int(self.port)))
        s.send(str(self.stream))
        s.close()
        
    def readStreamFromFile(self,fname):
        self.fname = fname
        
        f = open(fname,'r')
        stream = f.read()
        f.close()
        return stream
    