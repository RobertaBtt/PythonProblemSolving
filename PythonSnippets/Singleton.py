class Singleton:
    _instance = None
    def __new__(self):
        if self._instance is None:
            self._instance = super(Singleton, self).__new__(self)
        return  self._instance

a = Singleton()
b = Singleton()
c= Singleton()

print (id(a))

print (id(b))

print (id(c))