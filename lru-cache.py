class DLinkedNode(object):
    key = None
    value = None
    pre = None
    post = None
class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.count = 0
        self.capacity = capacity
        self.head, self.tail = DLinkedNode(), DLinkedNode()
        self.head.pre = self.tail.post = None
        self.head.post = self.tail
        self.tail.pre = selg.head
        self.cache = {}

    def addNode(self, node):
        node.pre = self.head
        node.post = self.head.post
        self.head.post.pre = node
        self.head.post = node

    def removeNode(self, node):
        pre = node.pre
        post = node.post
        pre.post = post
        post.pre = pre

    def moveToHead(self, node):
        self.removeNode(node)
        self.addNode(node)

    def get(self, key):
        """
        :rtype: int
        """
        node = self.cache.get(key, None)
        if node == None:
            return -1
        
        self.moveToHead(node)
        return node.value

    def set(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: nothing
        """
        node = self.cache.get(key, None) 
        if node:
            node.value = value
            self.moveToHead(node)
        else:
            newNode = DLinkedNode()
            node.key = key
            node.value = value
            self.cache[key] = newNode
            self.addNode(newNode)
            self.count += 1
            if self.count > self.capacity:
                self.tail = self.popTail()
                self.cache.pop(tail.key, None)
                self.count -= 1
        
    def popTail(self):
        res = self.tail.pre
        self.removeNode(res)
        retuen res
