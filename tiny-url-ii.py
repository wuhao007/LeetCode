class TinyUrl2:

    def __init__(self):
        self.id2url = {}
        self.url2id = {}
        self.custom_s2l = {}
        self.custom_l2s = {}

    def idToShortKey(self, id):
        ch = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
        s = ""
        while id > 0:
            s = ch[id % 62] + s
            id /= 62

        return (6 - len(s)) * 'a' + s

    def shortKeyToid(self, short_key):
        
        id = 0
        for c in short_key:
            if 'a' <= c <= 'z':
                id = id * 62 + ord(c) - ord('a')
            if 'A' <= c <= 'Z':
                id = id * 62 + ord(c) - ord('A') + 26
            if '0' <= c <= '9':
                id = id * 62 + ord(c) - ord('0') + 52

        return id
    # @param long_url a long url
    # @param a short key
    # @return a short url starts with http://tiny.url/
    def createCustom(self, long_url, short_key):
        # Write your code here
        short_url = "http://tiny.url/" + short_key

        id = self.shortKeyToid(short_key)

        if id in self.id2url and self.id2url[id] != long_url:
            return "error"

        if long_url in self.url2id and self.url2id[long_url] != id:
            return "error"

        if id in self.id2url or long_url in self.url2id:
            return short_url

        if short_url in self.custom_s2l and self.custom_s2l[short_url] != long_url:
            return "error"

        if long_url in self.custom_l2s and self.custom_l2s[long_url] != short_url:
            return "error"

        self.custom_l2s[long_url] = short_url
        self.custom_s2l[short_url] = long_url
        return short_url
    
    # @param {string} long_url a long url
    # @return {string} a short url starts with http://tiny.url/
    def longToShort(self, long_url):
        # Write your code here
        if long_url in self.custom_l2s:
            return self.custom_l2s[long_url]

        ans = 0
        if long_url in self.url2id:
            ans = self.url2id[long_url]
        else:
            for a in long_url:
                ans = (ans * 256 + ord(a)) % 56800235584L

        self.id2url[ans] = long_url
        self.url2id[long_url] = ans
        return "http://tiny.url/" + self.idToShortKey(ans)

    # @param {string} short_url a short url starts with http://tiny.url/
    # @return {string} a long url
    def shortToLong(self, short_url):
        # Write your code here
        if short_url in self.custom_s2l:
            return self.custom_s2l[short_url]

        short_key = short_url[len("http://tiny.url/"):]
        return self.id2url[self.shortKeyToid(short_key)]
