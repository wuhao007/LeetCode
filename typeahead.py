class Typeahead:

    # @param dict: A dictionary of words dict
    def __init__(self, dict):
        # do initialize if necessary
        self.mp = {}
        for s in dict:
            l = len(s)
            for i in xrange(l):
                for j in xrange(i + 1, l + 1):
                    tmp = s[i:j]
                    if tmp not in self.mp:
                        self.mp[tmp] = [s]
                    elif self.mp[tmp][-1] != s:
                        self.mp[tmp].append(s)

    # @param word: a string
    # @return a list of words
    def search(self, word):
        # write your code here
        if word not in self.mp:
            return []
        else:
            return self.mp[word]
