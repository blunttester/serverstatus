'''
Created on 31.7.2013

@author: janmatilainen
'''
import subprocess

class SrvStats(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        
    def cpu(self,appname):
        self.appname = appname
        """Return float containing CPU -usage used by defined application name."""
        
        self.process = subprocess.Popen("ps -o pcpu -p `ps -ef | grep -i %s | grep -v grep |grep -v Users| awk '{ print $2 }'`" % self.appname,
                                        shell=True,
                                        stdout=subprocess.PIPE,
                                        )
        self.cpu = self.process.communicate()[0].split('\n')
        
        if len(self.cpu) == 2 :
            return float(self.cpu[1])
        else:
            return "NO CPU INFO FOR " + str(self.appname)
    
    def top(self):
        """OS X TOP Uses different syntax and parameters than linux"""
        #self.process = subprocess.Popen("top -stats pid,rsize,vsize,cpu,th,pstate,time,command -o cpu -O +rsize -s 2 -n 10 -l 2| grep -A10 PID",
        self.process = subprocess.Popen("top -b -n 2 | grep -A10 PID",
                                        shell=True,
                                        stdout=subprocess.PIPE)
        self.top = self.process.communicate()[0].split('\n')
        """ Since the first captured top output does not contain the wanted data, we remove the first 13 elements""" 
        for x in xrange(12):
            del self.top[0]
        return self.top
        
    def appTop(self,appname):
        self.appname = appname

        self.app = subprocess.Popen("ps -ef | grep -i %s | grep -v grep |grep -v Users| awk '{ print $2 }'" % self.appname,
                                        shell=True,
                                        stdout=subprocess.PIPE)
        self.appPid = self.app.communicate()[0].split('\n')
        #print self.appPid[0]
        
#        self.process = subprocess.Popen("top -pid %s -stats pid,rsize,vsize,cpu,th,pstate,time,command -o cpu -O +rsize -s 2 -n 1 -l 2| grep -A10 PID" % self.appPid[0],
        self.process = subprocess.Popen("top -p%s -b -n 1| grep -A10 PID" % self.appPid[0],
                                        shell=True,
                                        stdout=subprocess.PIPE)
        self.appTop = self.process.communicate()[0].split('\n')
        return self.appTop[1]
    
    def mem(self, appname):
        self.appname = appname
        self.app = subprocess.Popen("ps -ef | grep -i %s | grep -v grep |grep -v Users| awk '{ print $2 }'" % self.appname,
                                        shell=True,
                                        stdout=subprocess.PIPE)
        self.appPid = self.app.communicate()[0].split('\n')
        #print self.appPid[0]
        
#        self.meminfo = subprocess.Popen("top -pid %s -stats rsize,vsize -s 2 -n 1 -l 2| grep -A2 RSIZE" % self.appPid[0],
        self.meminfo = subprocess.Popen("top -p%s -b -n 1| grep -A2 PID" % self.appPid[0],
                                        shell=True,
                                        stdout=subprocess.PIPE)
        self.appMem = self.meminfo.communicate()[0].split('\n')
        #print self.appMem
        return self.appMem            
        
