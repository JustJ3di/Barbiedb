from pyLittle_json import Json
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


    def store(self):
        js = Json(dict_obj = self.kv)
        js.serialize(f"{self.name}.json",mode='a')




COMMANDS = ["set","get","mset","mget","delete"]


class Server:
    def __init__(self, host = '127.0.0.1', port = 4231) -> None:
        self.host = host
        self.port = port
    
    def start(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind((self.host, self.port))
            s.listen()
            conn , addr = s.accept()
            with conn:
                while True:
                    conn.sendall("commands >>")
                    data = conn.recv(1024)
                    if not data:
                        break
                    
