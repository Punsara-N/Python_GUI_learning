## TCP server
from SocketServer import BaseRequestHandler, TCPServer
from threading import Thread

class RequestHandler(BaseRequestHandler):
    # override base class handle method
    def handle(self):
        print('Server connected to: ', self.client_address)
        while True:
            rsp = self.request.recv(512)
            if not rsp: break
            self.request.send(b'Server received: ' + rsp)

def startServer():
    serv = TCPServer(('', 24000), RequestHandler) # IP:'' is the same as 127.0.0.1, which is the localhost
    serv.serve_forever()
    
class OOP():
    def __init__(self):
        # Start TCP/IP server in its own thread
        svrT = Thread(target=startServer)
        svrT.setDaemon(True)
        svrT.start()
    
serverObject = OOP()