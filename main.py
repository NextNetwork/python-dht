import socket
from bencode import bencode,bdecode

BIND_IP = "0.0.0.0:9127"

class Krpc():
    def __init__(self):
        #self.socket.bind("0.0.0.0", self.port)
        return

class Client():
    def __init__(self):
        return

class Server():
    def __init__(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
        self.socket.bind(BIND_IP)
        return
    def start(self):
        while True:
            data, address = self.socket.recvfrom(1024)
            msg = bencode.bdecode(data)
            self.types[msg["y"]](msg, address)



if __name__ == 'main' :
    return
