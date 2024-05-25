import multiprocessing as mp

from socket import socket, AF_INET, SOCK_DGRAM


class UdpListener(mp.Process):
    def __init__(self, queue, host, port, buf):
        mp.Process.__init__(self)
        self.queue = queue
        self.addr = (host, port)
        self.buf = buf

    def run(self):
        UDPSock = socket(AF_INET, SOCK_DGRAM)
        UDPSock.bind(self.addr)

        while 1:
            data, addrs = UDPSock.recvfrom(self.buf)
            self.queue.put([data, addrs])
