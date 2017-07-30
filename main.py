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
MAX_PREFIX_LEN = 160

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
    def __init__(self, node):
        self.node = node
        self.nodeId = nodeId
        self.nodeIdLong = longInt(nodeId)
        self.rootBucket = Kbucket()
        return
    def append(self, node):
        nodeId = node.id
        #nodeIdLong = longInt(nodeId)
        for prefixLen in range(0, MAX_PREFIX_LEN - 1):
            div = prefixLen / 8 #the index of the node string
            mod = prefixLen % 8
            nodeIdDivInt = int(nodeId[div])
            # the high bit of nodeid & current prefixLen mod
            # when prifixlen = 0 ,then prifixlen mod = 0, highbit = 1000000 = 128 & nodeid[div]
            # the result = 1xxxxxx then >> (7-mod) = the high bit of byte(char)
            result = ((1 << (7 - mod)) & nodeIdDivInt) >> (7-mod)
            # get the child node of result index(0 or 1)
            childNode = self.rootBucket.childs[result]
            if childNode != None:
                #if child isn't null, continue find, because the node must be the end child
                self.rootBucket = childNode
            elif len(self.rootBucket) < K:
                # this bucket node isn't full
                self.rootBucket.append(node)

class Kbucket():
    def __init__(self):
        self.childs = []
        self.nodes = []
        self.prefix = 0

    def setChild(self, index, kbucket):
        self.child[index] = kbucket

    def append(self, node):
        self.nodes.append(node)

    def __len__(self):
        return len(self.nodes)

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
    nodeId = randomString(20)
    table = RoutingTable(nodeId)

    srv = Server(table)
    srv.start()

    cli = Client()
    cli.joinDHT()
