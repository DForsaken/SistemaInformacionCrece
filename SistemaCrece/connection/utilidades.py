import pickle
import math

class Utilidades:
    
    def __init__(self):
        self.infoSize = 4091
        self.packEsUltimoIndice = 1
        self.packTamIndice = 5
    
    def empaquetar(self, obj):
        print "empaquetar"
        return self.wrapperEmpaquetado(obj)
        
    def desempaquetar(self, obj):
        print "desmpaquetar"
        return pickle.loads(obj)
    
    def unWrapPaquete(self, obj):
        print "unwrapp Pquete "
        a = self.unwrapperEmpaquetado(obj)
        return a


    def wrapperEmpaquetado(self, obj):
        dumpObj = pickle.dumps(obj)
        lenDumpObj = len(dumpObj)
        if lenDumpObj < self.infoSize:
            numPacks = 1
        else:
            numPacks = math.ceil(lenDumpObj / self.infoSize)
        listPaquetes = []
        esUltimo = 0
        for i in range(0,numPacks):
            if lenDumpObj < (i*self.infoSize)+self.infoSize-1:
                tempDumpObj = dumpObj[i*self.infoSize:lenDumpObj]
                lenDumpObj = len(tempDumpObj)
                tamToFill = self.infoSize - lenDumpObj
                tempDumpObj += self.fillString(tamToFill)
            else:
                tempDumpObj = dumpObj[i*self.infoSize:(i*self.infoSize)+self.infoSize-1]
            if i == numPacks-1:
                esUltimo = 1 
            str2send = str(tempDumpObj + self.getStrDumpObjTam(str(lenDumpObj)) + str(esUltimo))
            listPaquetes.append(str2send) 
        return listPaquetes    
    
    def getStrDumpObjTam(self, dumpObjTam):
        tempStr = ""
        for i in range(len(dumpObjTam),4):
            tempStr += "0"
        return tempStr + dumpObjTam
    
    def fillString(self, tam):
        tempStr = ""
        for i in range(0,tam):
            tempStr += '0'
        return tempStr
    
    def unwrapperEmpaquetado(self, obj):
        tamObj = len(obj)
        esUltimo = int(obj[tamObj-self.packEsUltimoIndice:tamObj])
        tamInfo = int(obj[tamObj-self.packTamIndice:tamObj-self.packEsUltimoIndice])
        info = obj[:tamInfo]
        a = [info, esUltimo]  
        return a    
    
        
        
        
        
        
    