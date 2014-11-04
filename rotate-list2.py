class LRUCache:
    class Node:
        def __init__(self, key):
            self.prev = None
            self.next = None
            self.key = key
            
    # @param capacity, an integer
    def __init__(self):
        self.head = self.Node(-1, -1)
        self.tail = self.Node(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.hs = {}

    # @param key, an integer
    # @param value, an integer
    # @return nothing
    def set(self, key):
        if key in self.hs:
            current = self.hs[key]
            if current:
                current.prev.next = current.next
                current.next.prev = current.prev
            self.hs[key] = None
        else:
            insert = self.Node(key)

            insert.prev = self.tail.prev
            insert.next = self.tail
            self.tail.prev = insert
            insert.prev.next= insert

            self.hs[key] = insert
            
node = LRUCache
string = "jiang wen peipei doudou"
for s in string:
    node.set(s)

print node.head.next.value

