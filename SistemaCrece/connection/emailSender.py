'''
Created on 25/02/2014

@author: The Forsaken
'''

import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText

class emailSender:

    def __init__(self):
        self.fromaddr = ""
        self.smtpDom = ""
        self.smtpPort = -1
        self.passwd = ""
 
    def obtenerDatosIniciales(self):
        f = open("client.conf","r")
        i = 0
        for line in f.readlines():
            if i == 14:
                self.smtpDom = line.strip()
            elif i == 16:
                self.smtpPort = int(line.strip())
            elif i == 18:
                self.fromaddr = line.strip()
            elif i == 20:
                self.passwd = line.strip()
            i += 1
        
    def setMessage(self, strToSend, addr2send):
        self.msg = MIMEMultipart()
        self.msg['From'] = self.fromaddr
        self.msg['To'] = addr2send
        self.msg['Subject'] = "Recuperacion de contrasena"
        self.body = "Sistema Comunidad Crece : \n te enviamos tu contrasena " 
        self.body += strToSend[0] 
        self.body += " , si no sabes de que esto has caso omiso de este mensaje. \n\n Comunidad Crece A.C. "
        self.msg.attach(MIMEText(self.body, 'plain'))  
        
        
    def sendEmail(self, str2Send, addr2send):
        try:
            print "enviando !!", str2Send, addr2send
            self.setMessage(str2Send, addr2send)
            self.server = smtplib.SMTP('smtp.gmail.com', 587)
            self.server.ehlo()
            self.server.starttls()
            self.server.ehlo()
            self.server.login("alejandro.icss@gmail.com", "AngraStratodom")
            self.text = self.msg.as_string()
            self.server.sendmail(self.fromaddr, addr2send, self.text)
            print "mail enviado !!!"
            self.server.close()
        except Exception, e:
            return False
