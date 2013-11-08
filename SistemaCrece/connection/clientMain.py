import socket
from ui import PrincipalW
from PyQt4 import QtCore, QtGui
import sys
from utilidades import Utilidades

class clientMain:
  
    def __init__(self):
        self.host = "localhost"
        self.puerto = 5055     
        self.dataTypeFlag = 0   
        # 0 for string
        # 1 for table
        # 2 for comobox
        self.s = socket.socket()
        self.utilidad = Utilidades()            
        self.comenzarConexion()
        
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
            
                 
    def principal(self):
        self.app = QtGui.QApplication(sys.argv)
        self.p = PrincipalW.Principal()
        self.p.peticion.connect(self.procesarPeticion)
        sys.exit(self.app.exec_())                              
                  
    def enviarDatos(self, datos):
        self.s.send(self.utilidad.empaquetar(datos))
        print "enviando ", datos       
        
      
    def recibirDatos(self):
        # 0 for string
        # 1 for table
        # 2 for comobox
        self.s.setblocking(True)
        try:
            result = self.s.recv( 1024 )
            if self.dataTypeFlag == 1:
                print "si es tabla"
            elif self.dataTypeFlag == 2:
                print "si es combo"
            elif self.dataTypeFlag == 0:
                print "es string"
            if( None != result ):
                print "not none result"
                return self.utilidad.desempaquetar(result)
            return None
        except Exception, e:
            print e
        return ""
       
    #cada clase llama esta funcion para enviar al server 
    #datos -> tupla 
    def procesarPeticion(self):
        # 0 for string
        # 1 for table
        # 2 for comobox
        print self.p.args
        print self.p.dataTypeFlag
        self.dataTypeFlag = self.p.dataTypeFlag
        #test = pickle.dumps(list(self.p.args))
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
            elif self.dataTypeFlag == 0:
                print "es string"
    
    
c = clientMain()
#c.comenzarConexion()
    
    
    