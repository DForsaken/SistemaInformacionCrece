'''
Created on 03/07/2013

@author: The Forsaken
'''
import MySQLdb
from emailSender import emailSender
from PyQt4 import QtGui

class conexionDB:

    def __init__(self):    
        # connect
        self.host = "localhost"
        self.user = "root"
        self.passwd = "admin"
        self.dbName = "bdcrece"
        self.db = None
        self.cursor = None

    def obtenerDatosIniciales(self):        
        f = open("client.conf","r")
        i = 0
        for line in f.readlines():
            if i == 6:
                self.host = line.strip()
            elif i == 8:
                self.user = int(line.strip())
            elif i == 10:
                self.passwd = int(line.strip())
            elif i == 12:
                self.dbName = int(line.strip())
            i += 1
    def conectar(self):  
        print "conectando bd . . ."
        self.db = MySQLdb.connect(self.host, self.user, self.passwd, self.dbName)
        print "conectado a bd "
        print "cursor creado "
        
    def desconectar(self):
        self.cursor.close()
        self.db.close()
        print "desconectado bd "
        
    '''
        args -> tupla 3 elementos
        args[0] = nombre procedimiento
        args[1] = argumentos
        args[2] = tipo de retorno (tabla, string, comboBox)
    '''   
        
    def procesarQuery(self, args):   
        try:
            print "procesando query"
            self.cursor = self.db.cursor()
            print args[0]
            print args[1]
            print args[2]
            self.cursor.callproc(args[0], args[1])
            #if "ver" in args[0] or "actualiza" in args[0]:
            if "recuperarContrasena" in args[0]:
                self.email = emailSender()
                fetchRes = self.cursor.fetchall()
            elif "ver" in args[0]:
                fetchRes = self.cursor.fetchall()
                res = ()
                for i in self.cursor.description:
                    res = res + (i[0],)
                res = (res,)
                for i in fetchRes:
                    res = res + (i,) 
                print "RES - ", res
            self.cursor.close()
            self.db.commit()
            if args[2] == "tabla":
                print "procesarQuery Tabla"
                #self.obtenerTabla(res)
                print res
                return res
                #return self.obtenerTabla(res)
            elif args[2] == "comboBox":
                print res, " combo !!"
                return res               
            elif args[2] == "string":
                print "exitosa regresando string"
                return "Accion ejecutada correctamente"
            elif args[2] == "recoveryType":
                if len(fetchRes) == 0:
                    return "Error!, usuario o correo no validos"
                else:
                    if self.email.sendEmail(fetchRes[0], args[1][1]):
                        print "exitosa enviando mail"
                        return "Accion ejecutada correctamente"
                    else:
                        print "no pudo conectar"
                        return "Fallo conexion, verifique su conexion a internet"
            else: 
                return ""
        except Exception, e:
            print "a regresar ", e
            return e[1]

        


    