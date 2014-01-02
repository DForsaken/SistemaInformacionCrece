'''
Created on 03/07/2013

@author: The Forsaken
'''
import MySQLdb
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
            self.cursor.callproc(args[0], args[1])
            res = self.cursor.fetchall()
            #self.cursor.execute("call insertaArea('delirio')")
            self.cursor.close()
            self.db.commit()
            if args[2] == "tabla":
                print "procesarQuery Tabla"
                #self.obtenerTabla(res)
                print res
                return res
                #return self.obtenerTabla(res)
            elif args[2] == "combo":
                return self.obtenerCombo(res)               
            elif args[2] == "string":
                return "string"
            else: 
                return ""
        except Exception, e:
            print e

    
    def obtenerTabla(self, res):
        #results = cursor.fetchall()
        tabla = QtGui.QTableWidget()
        for row in range(0,len(res)):
            tabla.insertRow(row)
            record = res[row]                 
            for column in range (0,len(record)):                        
                newitem = QtGui.QTableWidgetItem(str(record[column]))
                tabla.setItem(row,column,newitem)
        print "obtener Tabla"        
        return res
                
    def obtenerCombo(self, res):
        #results = cursor.fetchall()
        for row in range(0,len(res)):
            self.dlg.ui.tblWtGIS.insertRow(row)
            record = res[row]                 
            for column in range (0,len(record)):                        
                newitem = QtGui.QTableWidgetItem(str(record[column]))
                self.dlg.ui.tblWtGIS.setItem(row,column,newitem)           
