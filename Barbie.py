from pyLittle_json import Json

class Barbie:

    '''
    class of storage "simple Json_object{key => value}

    operation set(key,value)

    operation get(key)->value

    '''
    
    log = []

    def __init__(self):
        self.me = {}
        self.list_key = []

    def set(self, **kwargs):
        '''
        perform a set of a key value on the db
        '''
        if len(kwargs.items()) > 1:
            return "error"
        for key, value in kwargs.items():
            self.me[key] = value
    
    
    def get(self, key):
        '''
        perform a search by a key
        '''
        return self.me.get(key)

    def store(self):
        pass







test_barbie = Barbie()

test_barbie.set(key = "vaòue")
test_barbie.set(new_key = "new_value")

print(test_barbie.get("key"))


