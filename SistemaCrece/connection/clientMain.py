import socket  
  
s = socket.socket()   
s.connect(("localhost", 5055))  
  
#while True:  
     # mensaje = raw_input("> ")  
s.send("asd")  
print s.recv(1024)
s.send("quitd")  
print s.recv(1024)
s.send("quit")
     # if mensaje == "quit":  
     #    break  
  
print "adios"  
s.shutdown(socket.SHUT_RDWR)
s.close() 