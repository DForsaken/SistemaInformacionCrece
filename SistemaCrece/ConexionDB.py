#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

class ConexionBD(object):

    def __init__(self, host="localhost", user="MyUser",passwd="MyPassword",
            db="crecebd")
        self.host = host
        self.user = user
        self.passwd = passwd

        # Unpack Other Database Arguments Here
        self.CreateConnection()

    def CreateConnection( self ):
        self.cursor = MySQLdb.connect(self.host, self.user, self.passwd)

    def DestroyConnection( self ):
        self.cursor.close()


