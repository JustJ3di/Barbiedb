import sys
from Barbie import Server

arv = sys.argv

ip = arv[1]
port = int(arv[2])


s = Server(ip,port).start()

