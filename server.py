from Barbie import Barbie
import socket

HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
PORT = 65432  # Port to listen on (non-privileged ports are > 1023)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    new = Barbie("new")
    with conn:
        print(f"Connected by {addr}")
        while True:
            data = conn.recv(1024)
            command = data.decode('utf-8')
            
            c_list = command.split()
            print(c_list)
            if not data:
                break
            elif c_list[0] == 'exit':
                break
            elif c_list[0] == 'set':
                new.set(c_list[1], c_list[2])
            elif c_list[0] == 'get':
                print("ciao")
                data = str(new.get(c_list[1])).encode('utf-8')
                
               
            conn.send(data)