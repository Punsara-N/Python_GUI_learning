from socket import socket, AF_INET, SOCK_STREAM
 
def writeToScrollText(inst):
    print("Hi from queue", inst)
    sock = socket(AF_INET, SOCK_STREAM)
    sock.connect(('localhost', 24000))
    for i in range(10):
        sock.send(b'Message from a queue: ' + bytes(str(i).encode()))
        recv = sock.recv(8192).decode()
        inst.guiQueue.put(recv)
    inst.createThread()