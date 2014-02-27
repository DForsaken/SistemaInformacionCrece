#!/usr/bin/env python
# -*- coding: utf8 -*-

import sys
import socket
import threading
import time
import conexionBD
from PyQt4 import QtGui
from utilidades import Utilidades

QUIT = False

class ClientThread( threading.Thread ):
    '''
    Class that implements the client threads in this server
    '''   

    def __init__( self, client_sock ):
        '''
        Initialize the object, save the socket that this thread will use.
        '''
        self.firstRead = True
        threading.Thread.__init__( self )
        self.client = client_sock
        self.utilidad = Utilidades()     
        self.packTam = 4096
        
    def run( self ):
        '''
        Thread's main loop. Once this function returns, the thread is finished
        and dies.
        '''
        print "start"
        #
        # Need to declare QUIT as global, since the method can change it
        #
        global QUIT
        done = False   
        #
        # Read data from the socket and process it
        #
        
        while not done:
            try:
                #handshake 
                if self.firstRead :
                    self.firstRead = False
                    cmd = self.readline()
                    print "comunidad readline", cmd
                    if 'comunidad' == cmd: 
                        self.writeline("crece")
                        print "enviando crece"
                    elif cmd == None:
                        print "no crece"
                else:
                    if 'quit' == cmd :
                        self.writeline( 'Ok, bye' )
                        QUIT = True
                        done = True
                    elif 'bye' == cmd:
                        done = True
                    else:                    
                        cmd = self.readline()    
                        if cmd != None and cmd != "":
                            print " entro CMD " , cmd
                            res = self.procesarPeticion(cmd)      
                            if res != "":
                                self.writeline(res)
            except socket.error, e:
                print "error de conexion"
        #
        # Make sure the socket is closed once we're done with it
        #
        self.client.close()
        return

    def readline( self ):
        '''
        Helper function, reads up to 64000 chars from the socket, and returns
        them as a string, all letters in lowercase, and without any end of line
        markers '''
        self.client.setblocking(True)
        resultado = []
        objSerializado = ""
        #while(True):
        try:
            res = self.client.recv( self.packTam )
            f = open("test", "w")
            f.write(res)
            f.close()
            print "len", len(res)
            print "res ", res
            resultado = self.utilidad.unWrapPaquete(res)
            print "resultado ", resultado
            objSerializado += resultado[0] 
            if resultado[1] == 1:
                print "fue uno"
                if None != objSerializado or objSerializado == "":
                    print "retornando", objSerializado
                    return self.utilidad.desempaquetar(objSerializado)
        except Exception, e:
            print e
        return None
    
    def writeline( self, text ):
        '''
        Helper function, writes teh given string to the socket, with an end of
        line marker appended at the end
        '''
        listObjEnviar = self.utilidad.empaquetar(text)
        print "voy a escribir !!! - ", len(listObjEnviar)
        for i in range(0, len(listObjEnviar)):
            self.client.send(listObjEnviar[i])     
    
    def procesarPeticion(self, args):
        #separa la informacion en 3 partes
        
        print "procesar peticion server"
        conexion = conexionBD.conexionDB()
        conexion.conectar()
        res = conexion.procesarQuery(args)
        conexion.desconectar()
        print "regresando res"
        return res
        
    
           

class Server:
    '''
    Server class. Opens up a socket and listens for incoming connections.
    Every time a new connection arrives, it creates a new ClientThread thread
    object and defers the processing of the connection to it.
    '''

    def __init__( self ):
        self.sock = None
        self.thread_list = []

    def run( self ):
        '''
        Server main loop.
        Creates the server (incoming) socket, and listens on it of incoming
        connections. Once an incomming connection is deteceted, creates a
        ClientThread to handle it, and goes back to listening mode.
        '''
        
        all_good = False
        try_count = 0

        #
        # Attempt to open the socket
        #
        while not all_good:
            if 3 < try_count:
                #
                # Tried more than 3 times, without success... Maybe the port
                # is in use by another program
                #
                sys.exit( 1 )
            try:
                #
                # Create the socket
                #
                self.sock = socket.socket( socket.AF_INET, socket.SOCK_STREAM )
                
                #
                # Bind it to the interface and port we want to listen on
                #
                address = ""
                port = -1
                f = open("server.conf","r")
                i = 0
                for line in f.readlines():
                    if i == 2:
                        address = line.strip()
                    elif i == 4:
                        port = int(line.strip())
                    i += 1
                print address, "-", port
                self.sock.bind( ( address, port ) )            
                #
                # Listen for incoming connections. This server can handle up to
                # 5 simultaneous connections
                #
                self.sock.listen( 15 )
                self.sock.setblocking(True)
                all_good = True
                break
            except socket.error, err:
                #
                # Could not bind on the interface and port, wait for 10 seconds
                #
                print 'Socket connection error... Waiting 10 seconds to retry.'
                del self.sock
                time.sleep( 10 )
                try_count += 1

        print "Server is listening for incoming connections."
        print
        print "typing 'bye' finishes the thread, but not the server ",
        print "(eg. you can quit telnet, run it again and get a different ",
        print "thread name"
        print "typing 'quit' finishes the server"

        try:
            #
            # NOTE - No need to declare QUIT as global, since the method never
            #    changes its value
            #
            while not QUIT:
                try:
                    #
                    # Wait for half a second for incoming connections
                    #
                    self.sock.settimeout( 0.500 )
                    client = self.sock.accept()[0]
                except socket.timeout:
                    #
                    # No connection detected, sleep for one second, then check
                    # if the global QUIT flag has been set
                    #
                    time.sleep( 1 )
                    if QUIT:
                        print "Received quit command. Shutting down..."
                        break
                    continue
                #
                # Create the ClientThread object and let it handle the incoming
                # connection
                #
                new_thread = ClientThread( client )
                print 'Incoming Connection. Started thread ',
                print new_thread.getName()
                self.thread_list.append( new_thread )
                
                new_thread.start()

                #
                # Go over the list of threads, remove those that have finished
                # (their run method has finished running) and wait for them
                # to fully finish
                #
                for thread in self.thread_list:
                    if not thread.isAlive():
                        self.thread_list.remove( thread )
                        thread.join()

        except KeyboardInterrupt:
            print 'Ctrl+C pressed... Shutting Down'
        except Exception, err:
            print 'Exception caught: %s\nClosing...' % err

        #
        # Clear the list of threads, giving each thread 1 second to finish
        # NOTE: There is no guarantee that the thread has finished in the
        #    given time. You should always check if the thread isAlive() after
        #    calling join() with a timeout paramenter to detect if the thread
        #    did finish in the requested time
        #
        for thread in self.thread_list:
            thread.join( 1.0 )
        #
        # Close the socket once we're done with it
        #
        self.sock.close()

        

