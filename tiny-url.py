class TinyUrl:
    
    def __init__(self):
        self.dict = {}
        
    def getShortKey(self, url):
        return url[-6:]
        
    def idToShortKey(self, id):
        ch = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
        s = ""
        while id > 0:
            s = ch[id % 62] + s
            id /= 62
        return 'a' * (6-len(s)) + s

    def shortkeyToid(self, short_key):
        id = 0
        for c in short_key:
            if 'a' <= c <= 'z':
                id = id * 62 + ord(c) - ord('a')
            if 'A' <= c <= 'Z':
                id = id * 62 + ord(c) - ord('A') + 26
            if '0' <= c <= '9':
                id = id * 62 + ord(c) - ord('0') + 52
        return id
                
    # @param {string} url a long url
    # @return {string} a short url starts with http://tiny.url/
    def longToShort(self, url):
        # Write your code here
        ans = 0
        for a in url:
            ans = (ans * 256 + ord(a)) % 56800235584L
        
        while ans in self.dict and self.dict[ans] != url:
            ans += 1
        
        self.dict[ans] = url
        return "http://tiny.url/" + self.idToShortKey(ans)

    # @param {string} url a short url starts with http://tiny.url/
    # @return {string} a long url
    def shortToLong(self, url):
        # Write your code here
        short_key = self.getShortKey(url)
        return self.dict[self.shortkeyToid(short_key)]

