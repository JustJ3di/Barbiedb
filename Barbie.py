#from pyLittle_json import Json
import socket

class Barbie:

    '''
    class of storage "simple Json_object{key => value}

    operation set(key,value)

    operation get(key)->value

    '''
    
    log = []

    def __init__(self,Name:str):
        self.kv = {}
        self.name = Name
        self.log.append(f"create db {Name}")

    def set(self, key, value):
        self.kv[key] = value
        
    
    
    def get(self, key):
        '''
        perform a search by a key
        '''
        return self.kv.get(key)

    def delete(self, key):
        if key in self.kv:
            del self.kv[key]
            return True
        else:
            return False

    '''
    def store(self):
        js = Json(dict_obj = self.kv)
        js.serialize(f"{self.name}.json",mode='a')
    '''





class Server:
    def __init__(self, host = '127.0.0.1', port = 4231) -> None:
        self.host = host
        self.port = port
    
    def start(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind((self.host, self.port))
            s.listen()
            conn, addr = s.accept()
            new = Barbie("new")
            with conn:
                print(f"Connected by {addr}")
                while True:
                    data = conn.recv(1024)
                    command = data.decode('utf-8')
                    c_list = command.split("$")
                    if not data:
                        break
                    elif c_list[0] == 'exit':
                        break
                    elif c_list[0] == 'set':
                        new.set(c_list[1], c_list[2])
                    elif c_list[0] == 'get':
                        data = str(new.get(c_list[1])).encode('utf-8')
                    elif c_list[0] == 'delete':
                        new.delete(c_list[1])
                        
                    conn.send(data)


class Client:
    def __init__(self, host = '127.0.0.1', port = 4231) -> None:
        self.host = host
        self.port = port
    def start(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((self.host, self.port))
            while True:
                c = input("comma>>>")
            
                s.send(c.encode('utf-8'))     
                data = s.recv(1024)
                data = data.decode('utf-8')
                print(f"{data}")
                if data == 'exit':
                    break
               