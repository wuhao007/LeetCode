class LFUCache:

    # @param capacity, an integer
    def __init__(self, capacity):
        # write your code here
        self.cache = {}
        self.frequencyList = [collections.OrderedDict() for _ in range(maxFrequency + 1)]
        self.lowestFrequency = 0
        self.maxFrequency = capacity * 2 - 1
        self.maxCacheSize = capacity


    # @param key, an integer
    # @param value, an integer
    # @return nothing
    def set(self, key, value):
        # write your code here
        currentNode = self.cache.get(key, None)
        if currentNode:
            currentNode.v = value
        else:
            if len(cache) == self.maxCacheSize:
                self.doEviction()

    def doEviction(self):
        currentlyDeleted = 0
        target = 1
        while currentlyDeleted < target:
            nodes = self.frequencyList[self.lowestFrequency]
            if nodes:
                while self.cache and currentlyDeleted < target:
                    currentlyDeleted += 1
                    self.cache.popitem(False) ###
                if not self.cache:
                    self.findNextLowestFrequency() 

    def findNextLowestFrequency():
        while self.lowestFrequency <= maxFrequency and not frequencyList[lowestFrequency]:
            self.lowestFrequency += 1
        if self.lowestFrequency > self.maxFrequency:
            self.lowestFrequency = 0
    
            
                

    # @return an integer
    def get(self, key):
        # write your code here

class CacheNode:
    def __init__(self, k, v, frequency):
        self.k = k
        self.v = v
        self.frequency = frequency
