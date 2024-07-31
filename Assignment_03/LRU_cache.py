# LRU ( Least Recently used ) cache uses Doubly linked list & hashmap

class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}  # hashmap to store key -> Node
        self.head = Node(0, 0)  # dummy head
        self.tail = Node(0, 0)  # dummy tail
        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove(self, node: Node):
        # remove an existing node from the linked list
        prev = node.prev
        nxt = node.next
        prev.next = nxt
        nxt.prev = prev

    def _add(self, node: Node):
        # add a new node right after the head
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self._remove(node)
            self._add(node)
            return node.value
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self._remove(self.cache[key])
        node = Node(key, value)
        self._add(node)
        self.cache[key] = node
        if len(self.cache) > self.capacity:
            # remove from the linked list and delete the LRU from the hashmap
            lru = self.tail.prev
            self._remove(lru)
            del self.cache[lru.key]

#--------------------------------Implementation 
lru_cache = LRUCache(2)
lru_cache.put(1, 1)
lru_cache.put(2, 2)
print(lru_cache.get(1))  # returns 1
lru_cache.put(3, 3)      # evicts key 2
print(lru_cache.get(2))  # returns -1 (not found)
lru_cache.put(4, 4)      # evicts key 1
print(lru_cache.get(1))  # returns -1 (not found)
print(lru_cache.get(3))  # returns 3
print(lru_cache.get(4))  # returns 4
