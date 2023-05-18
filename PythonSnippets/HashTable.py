class HashTable(object):

    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(self.size)]

    def get_table(self):
        return self.table

hash_table = HashTable(10)
print(hash_table.get_table())

