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
        file=open("servertest", "w")
        file.write(dumpObj)
        file.close()
        #print ' a comparar Empa', dumpObj
        #print 'a delirar Empa', pickle.loads(dumpObj)
        lenDumpObj = len(dumpObj)
        if lenDumpObj < self.infoSize:
            numPacks = 1
        else:
            numPacks = int(math.ceil(float(lenDumpObj) / float(self.infoSize)))
        listPaquetes = []
        esUltimo = 0
        for i in range(0,numPacks):
            if lenDumpObj < (i*self.infoSize)+self.infoSize-1:
                tempDumpObj = dumpObj[i*self.infoSize:lenDumpObj]
                lenDumpObj = len(tempDumpObj)
                tamToFill = self.infoSize - lenDumpObj
                print "lenDumpObj2", len(tempDumpObj), " - ", str(lenDumpObj), " - ", tamToFill
                tempDumpObj += self.fillString(tamToFill)
                str2send = tempDumpObj + self.getStrDumpObjTam(str(lenDumpObj))
                print "str2send lenDumpObj2 ", len(tempDumpObj), " - ", len(self.getStrDumpObjTam(str(lenDumpObj)))
            else:
                tempDumpObj = dumpObj[i*self.infoSize:(i*self.infoSize)+self.infoSize]
                print "lenDumpObj1", len(tempDumpObj), " - ", str(self.infoSize-1)
                str2send = tempDumpObj + self.getStrDumpObjTam(str(self.infoSize))
            if i == numPacks-1:
                esUltimo = 1 
            str2send += str(esUltimo)
            listPaquetes.append(str2send) 
        print "imprimiendo paquetes"
        for i in listPaquetes:
            print "-", len(i)
        self.delirar(listPaquetes)
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
        try:
            tamObj = len(obj)
            esUltimo = int(obj[tamObj-self.packEsUltimoIndice:tamObj])
            tamInfo = int(obj[tamObj-self.packTamIndice:tamObj-self.packEsUltimoIndice])
            info = obj[:tamInfo]
            a = [info, esUltimo]  
            print " -sdfsd- ", tamInfo, " - " , esUltimo
            return a    
        except Exception, e:
            print e
    def delirar(self, paquetes):
        objSerializado = ""
        for i in paquetes:
            resultado = self.unwrapperEmpaquetado(i)
            objSerializado += resultado[0]
            if resultado[1] == 1:
                break    
        a = pickle.loads(objSerializado)
    