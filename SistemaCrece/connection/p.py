import sys
import pickle
import threading

class d( threading.Thread ):
    '''
    Class that implements the client threads in this server
    '''   

    def __init__(self):
        print "empezando"
        threading.Thread.__init__( self )
        
        
    def run( self ):
        print "start"
        l = pickle.dumps('adsf')       
        d = pickle.loads(l)
        print d


ddd = d()
ddd.start()       