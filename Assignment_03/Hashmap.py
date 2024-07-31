

# HashMap with Open addressing --------------------------------------------------------

class OpenAddressingHashMap:
    def __init__(self, size=100, probing='linear'):
        self.size = size
        self.table = [None] * size
        self.probing = probing

    def hash_function(self, key):
        return hash(key) % self.size

    def _probe(self, key, i):
        if self.probing == 'linear':
            return (self.hash_function(key) + i) % self.size
        elif self.probing == 'quadratic':
            return (self.hash_function(key) + i ** 2) % self.size

    def insert(self, key, value):
        i = 0
        while i < self.size:
            index = self._probe(key, i)
            if self.table[index] is None or self.table[index] == 'deleted':
                self.table[index] = (key, value)
                return
            i += 1
        raise Exception("HashMap is full")

    def find(self, key):
        i = 0
        while i < self.size:
            index = self._probe(key, i)
            if self.table[index] is None:
                return False
            if self.table[index] != 'deleted' and self.table[index][0] == key:
                return True
            i += 1
        return False

    def remove(self, key):
        i = 0
        while i < self.size:
            index = self._probe(key, i)
            if self.table[index] is None:
                return
            if self.table[index] != 'deleted' and self.table[index][0] == key:
                self.table[index] = 'deleted'
                return
            i += 1

#-------------------------------------------------------------------------------------------------------

# HashMap with Separate chaining

class SeparateChainingHashMap:
    def __init__(self, size=100):
        self.size = size
        self.table = [[] for _ in range(size)]

    def hash_function(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        index = self.hash_function(key)
        for i, (k, v) in enumerate(self.table[index]):
            if k == key:
                self.table[index][i] = (key, value)
                return
        self.table[index].append((key, value))

    def find(self, key):
        index = self.hash_function(key)
        for k, v in self.table[index]:
            if k == key:
                return True
        return False

    def remove(self, key):
        index = self.hash_function(key)
        for i, (k, v) in enumerate(self.table[index]):
            if k == key:
                self.table[index].pop(i)
                return
#-------------------------------------------------------------------------------------------------------------

# Implementation 

# Open Addressing with Linear Probing
oa_hashmap = OpenAddressingHashMap(size=10, probing='linear')
oa_hashmap.insert("key1", "value1")
print(oa_hashmap.find("key1"))  # True
oa_hashmap.remove("key1")
print(oa_hashmap.find("key1"))  # False

# Separate Chaining
sc_hashmap = SeparateChainingHashMap(size=10)
sc_hashmap.insert("key1", "value1")
print(sc_hashmap.find("key1"))  # True
sc_hashmap.remove("key1")
print(sc_hashmap.find("key1"))  # False
