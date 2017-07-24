import socket
from utils import *
from bencode import bencode,bdecode

BIND_IP = "0.0.0.0:9127"
K = 8
TID_LENGTH = 4
DHT_ROUTER_NODES = [
    ('router.bittorrent.com', 6881),
    ('router.utorrent.com', 6881),
    ('router.bitcomet.com', 6881),
    ('dht.transmissionbt.com', 6881)
]

class Krpc():
    def __init__(self):
        #self.socket.bind("0.0.0.0", self.port)
        return

    @staticmethod
    def sendKrpc(socket, msg, addr):
        try:
            socket.sendto(bencode(msg), addr)
        except Exception,e:
            pass

class Client():
    def __init__(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        return
    def joinDHT(self):
        for addr in DHT_ROUTER_NODES:
            self.findNode(addr, self.table.nid)
    def findNode(self, addr, target):
        tid = randomString(TID_LENGTH)
        msg = {
            "t": tid,
            "y": "q",
            "q": "find_node",
            "a": {"id": self.table.nid, "target": target}
        }
        Krpc.send_krpc(self.socket, msg, addr)
        return

class Server():
    def __init__(self, table):
        types = {
            "r": self.response(),
            "q": self.request(),
        }

        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
        self.socket.bind(BIND_IP)
        self.table = table

        return
    def start(self):
        while True:
            data, address = self.socket.recvfrom(1024)
            msg = bencode.bdecode(data)
            self.types[msg["y"]](msg, address)
    def request(self, msg, addr):
        return
    def response(self, msg, addr):
        return

class RoutingTable():
    def __init__(self):
        return
class Kbucket():
    def __init__(self):
        return
class Node(object):
    __slots__ = ("nid", "ip", "port")
    def __init__(self, nid, ip, port):
        self.nid = nid
        self.ip = ip
        self.port = port
    def __eq__(self, other):
        return self.nid == other.nid


if __name__ == '__main__':
    #my node id
    myNodeId = randomString(20)
    table = RoutingTable()

    srv = Server(table)
    srv.start()

    cli = Client()
    cli.joinDHT()
