class Resource:
    def __init__(self, value, expired):
        self.value = value
        self.expired = expired

INT_MAX = 0x7fffffff

class Memcache:

    def __init__(self):
        # initialize your data structure here.
        self.client = {}
    
    # @param {int} curtTime an integer
    # @param {int} key an integer
    # @return an integer
    def get(self, curtTime, key):
        # Write your code here
        if key not in self.client:
            return INT_MAX
        res = self.client.get(key)
        if res.expired >= curtTime or res.expired == -1:
            return res.value
        return INT_MAX

    # @param {int} curtTime an integer
    # @param {int} key an integer
    # @param {int} integer
    # @param {int} ttl an integer
    # @return nothing
    def set(self, curtTime, key, value, ttl):
        # Write your code here
        if ttl:
            res = Resource(value, curtTime + ttl - 1)
        else:
            res = Resource(value, -1)
        self.client[key] = res
        
    # @param {int} curtTime an integer
    # @param {int} key an integer
    # @return nothing
    def delete(self, curtTime, key):
        # Write your code here
        if key not in self.client:
            return
        del self.client[key]

    # @param {int} curtTime an integer
    # @param {int} key an integer
    # @param {int} delta an integer
    # @return an integer
    def incr(self, curtTime, key, delta):
        # Write your code here
        if key not in self.client:
            return INT_MAX

        self.client[key].value += delta
        return self.get(curtTime, key)

    # @param {int} curtTime an integer
    # @param {int} key an integer
    # @param {int} delta an integer
    # @return an integer
    def decr(self, curtTime, key, delta):
        # Write your code here
        if key not in self.client:
            return INT_MAX
        self.client[key] -= delta
        return self.get(curtTime, key)
