
class Barbie:
    
    log = []

    def __init__(self):
        self.key = []
        self.value = []

    def set(self, **kwargs):
        '''
        perform a set of a key value on the db
        '''


        for key, value in kwargs.items():
            self.key.append(key)
            self.value.append(value)
        
    
    def get(self, key):
        '''
        perform a search by a key
        '''
        try:
            return self.value[self.key.index(key)]
        except:
            return "error no value for this key"

    def store(self):
        pass







test_barbie = Barbie()

test_barbie.set(key = "vaòue")
test_barbie.set(new_key = "new_value")

print(test_barbie.get("key"))


