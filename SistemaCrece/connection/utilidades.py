import pickle

class Utilidades:
    
    def empaquetar(self, obj):
        print "empaquetar"
        return pickle.dumps(obj)
    
    def desempaquetar(self, obj):
        print "desmpaquetar"
        return pickle.loads(obj)
