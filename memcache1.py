class Memcache:

    def __init__(self):
        self.mp = {}

    def get(self, curtTime, key): 
        temp = None
        if key in self.mp:
            temp = self.mp[key]
        else:
            return 2147483647

        if curtTime >= temp[1] and temp[1] != 0: 
            return 2147483647
        else:
            return temp[0]

    def set(self, curtTime, key, value, ttl): 
        expire = 0 if ttl == 0 else curtTime + ttl
        val = (value, expire)
        self.mp[key] = val
    
    def delete(self, curtTime, key): 
        if key in self.mp:
            self.mp.pop(key, None)

    def incr(self, curtTime, key, delta): 
        if key not in self.mp:
            return 2147483647
        
        if curtTime >= self.mp[key][1] and self.mp[key][1] != 0: 
            #self.mp.pop(key, None)
            return 2147483647
        else:
            temp = self.mp[key][0]
            temp += delta
            val = (temp, self.mp[key][1])
            self.mp[key] = val
            return temp
        
    

    def decr(self, curtTime, key, delta): 
        if key not in self.mp:
            return 2147483647
        
        if curtTime >= self.mp[key][1] and self.mp[key][1] != 0:
            #self.mp.pop(key, None)
            return 2147483647
        else: 
            temp = self.mp[key][0]
            temp -= delta
            val = (temp, self.mp[key][1])
            self.mp[key] = val
            return temp
