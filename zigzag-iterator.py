class ZigzagIterator(object):

    def __init__(self, v1, v2):
        """
        Initialize your data structure here.
        :type v1: List[int]
        :type v2: List[int]
        """
        self.v1 = v1
        self.v2 = v2
        self.i = 0
        self.j = 0
        

    def next(self):
        """
        :rtype: int
        """
        if self.i == len(self.v1):
            self.j += 1
            return self.v2[self.j]
        elif self.j == len(self.v2) - 1:
            self.i += 1
            return self.v1[self.i]
        elif self.i < self.j:
            self.i += 1
            return self.v1[self.i]
        else:
            self.j += 1
            return self.v2[self.j]

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.i < len(self.v1) or self.j < len(self.v2)
            
        

# Your ZigzagIterator object will be instantiated and called as such:
# i, v = ZigzagIterator(v1, v2), []
# while i.hasNext(): v.append(i.next())
