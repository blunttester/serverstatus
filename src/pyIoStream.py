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
        data = s.recv(1024)
        print str(data)

        s.close()
        
    def readStreamFromFile(self,fname):
        self.fname = fname
        
        f = open(fname,'r')
        stream = f.read()
        f.close()
        return stream
    
    def writeStreamToMongo(self,top, *args, **kwargs):
        import json
        import pymongo
        from bson.objectid import ObjectId
        
        self.top = top
        
        connection = pymongo.Connection()
        
        db = connection["serverstats"]
        tops = db["top"]
        
        def json_list(list):
            lst = []
            d = {}
            for pn in list:
                d['top']=pn
                lst.append(d)
            return json.dumps(lst, separators=(',',':'))

        print json_list(str(self.top))
        
        #tops.insert(json_list(self.top))

    def writeStreamToSqlite(self,*args, **kwargs):
        
        self.stuff = str(args).split(',')
        for x in xrange(len(self.stuff)):
            print self.stuff[x]
        
        return 'DONE'
        