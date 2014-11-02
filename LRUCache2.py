class LRUCache:
    class Node:
        def __init__(self, key):
            self.prev = None
            self.next = None
            self.key = key
            self.value = 1
            
    # @param capacity, an integer
    def __init__(self):
        self.head = self.Node(-1)
        self.tail = self.Node(-1)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.hs = {}

    # @param key, an integer
    # @param value, an integer
    # @return nothing
    def set(self, key):
        if key in self.hs:
            self.hs[key].value += 1
        else:
            insert = self.Node(key)

            insert.prev = self.tail.prev
            insert.next = self.tail
            self.tail.prev = insert
            insert.prev.next = insert

            self.hs[key] = insert
            
node = LRUCache()
string = "appleE"
for s in string:
    node.set(s)

root = node.head.next
while root:
    print root.key, root.value
    root = root.next
