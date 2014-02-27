import socket
from ui import PrincipalW
from PyQt4 import QtCore, QtGui
import sys
from utilidades import Utilidades

class clientMain:
  
    def __init__(self):
        self.host = ""
        self.puerto = -1     
        self.obtenerDatosIniciales()
        self.dataTypeFlag = 0  
        self.packTam = 4096
        # 0 for string
        # 1 for table
        # 2 for comobox
        self.s = socket.socket()
        self.utilidad = Utilidades()            
        self.comenzarConexion()
    
    def obtenerDatosIniciales(self):
        f = open("client.conf","r")
        i = 0
        for line in f.readlines():
            if i == 2:
                self.host = line.strip()
            elif i == 4:
                self.puerto = int(line.strip())
            i += 1
    
    def comenzarConexion(self):      
        print "comenzando conexion "
        try:        
            print "conectando"
            self.s.connect((self.host, self.puerto))  
            self.enviarDatos("comunidad")  
            cmd = self.recibirDatos()
            print "cmd -> ", cmd
            if "crece" !=  cmd:
                self.enviarDatos("quit")              
                print "No pudo conectarse a server"  
                self.s.shutdown(socket.SHUT_RDWR)
                self.s.close() 
            print "principal"
            self.principal()
        except Exception, e:
            print "Error : "  , e 
            
    def terminarConexion(self):
        self.enviarDatos("bye")
        sys.exit(0)
        
    def principal(self):
        print "abriendo ..."
        self.app = QtGui.QApplication(sys.argv)
        self.p = PrincipalW.Principal()
        self.p.peticion.connect(self.procesarPeticion)
        self.p.closed.connect(self.terminarConexion)
        sys.exit(self.app.exec_())                              
                  
    def enviarDatos(self, datos):      
        listObjEnviar = self.utilidad.empaquetar(datos)
        for i in range(0, len(listObjEnviar)):
            print "len enviado - ", listObjEnviar[i]
            self.s.send(listObjEnviar[i])
        print "enviando ", datos            
            
    def recibirDatos(self):
        # 0 for string
        # 1 for table
        # 2 for comobox
        self.s.setblocking(True)
        resultado = []
        objSerializado = ""
        while(True):
            try:
                resultado = self.utilidad.unWrapPaquete(self.s.recv( self.packTam ))
                objSerializado += resultado[0]
                if resultado[1] == 1:
                    break
            except Exception, e:
                print "exception recibirDatos " , e
                return None
        if self.dataTypeFlag == 1:
            print "si es tabla"
        elif self.dataTypeFlag == 2:
            print "si es combo"
        elif self.dataTypeFlag == 0:
            print "es string"
        if( None != objSerializado ):
            print "not none result"
        return self.utilidad.desempaquetar(objSerializado)
        
       
    #cada clase llama esta funcion para enviar al server 
    #datos -> tupla 
    def procesarPeticion(self):
        # 0 for string
        # 1 for table
        # 2 for comobox
        try:
            print self.p.args
            print self.p.dataTypeFlag
            self.dataTypeFlag = self.p.dataTypeFlag
            print "enviando datos"
            self.enviarDatos(self.p.args)
            if self.p.args[2] == "":
                return None
            else:
                print "regresando datos"
                if self.dataTypeFlag == 1:
                    print "si es tabla"
                    self.p.obtenerTabla(self.recibirDatos())
                elif self.dataTypeFlag == 2:
                    print "si es combo"
                    self.p.obtenerComboBox(self.recibirDatos())
                elif self.dataTypeFlag == 0:
                    print "es string"
                    temp = str(self.recibirDatos())
                    print temp, " - temp"
                    if temp == "Accion ejecutada correctamente":
                        self.p.mostrarMensaje(temp, 0)
                    else:
                            self.p.mostrarMensaje(temp, 1)
        except socket.error, e:
            QtGui.QMessageBox.critical(self, 'Error Fatal!!!!', 
                            "Se ha perdido la conexion con el servidor, reinicie el programa", 
                            QtGui.QMessageBox.Ok)            
    
    
c = clientMain()
#c.comenzarConexion()
    
    
    