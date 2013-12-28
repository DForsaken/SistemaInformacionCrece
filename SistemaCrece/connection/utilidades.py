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
        print "a - ",  a
        return a


    def wrapperEmpaquetado(self, obj):
        print obj        
        dumpObj = pickle.dumps(obj)
        print dumpObj
        print "len d ", len(dumpObj)
        print "dump - ", dumpObj
        lenDumpObj = len(dumpObj)
        if lenDumpObj < self.infoSize:
            numPacks = 1
        else:
            numPacks = math.ceil(lenDumpObj / self.infoSize)
        listPaquetes = []
        esUltimo = 0
        print "numero de paquetes", numPacks
        for i in range(0,numPacks):
            if lenDumpObj < (i*self.infoSize)+self.infoSize-1:
                tempDumpObj = dumpObj[i*self.infoSize:lenDumpObj]
                lenDumpObj = len(tempDumpObj)
                tamToFill = self.infoSize - lenDumpObj
                print "len te ", len(tempDumpObj), " - ", tamToFill, " - ", tempDumpObj
                tempDumpObj += self.fillString(tamToFill)
                print "len tempDumpObj ", len(tempDumpObj)
            else:
                tempDumpObj = dumpObj[i*self.infoSize:(i*self.infoSize)+self.infoSize-1]
            if i == numPacks-1:
                esUltimo = 1 
            str2send = str(tempDumpObj + self.getStrDumpObjTam(str(lenDumpObj)) + str(esUltimo))
            print "str Ultimo ", len(str2send)
            listPaquetes.append(str2send) 
            print listPaquetes[i]
            print "len ", len(listPaquetes[i]), " len ", lenDumpObj
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
        print "llamada"
        print " len loaded ", len(obj)
        print "loaded -- ", obj
        tamObj = len(obj)
        esUltimo = int(obj[tamObj-self.packEsUltimoIndice:tamObj])
        print "esUltimo ", esUltimo
        tamInfo = int(obj[tamObj-self.packTamIndice:tamObj-self.packEsUltimoIndice])
        print "tamInfo ",tamInfo 
        info = obj[:tamInfo]
        print "info ", info
        a = [info, esUltimo]  
        print "des ", a
        return a    
    
        
        
        
        
        
    