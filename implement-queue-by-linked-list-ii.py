class Node():
    def __init__(self, _val):
        self.prev = self.next = None
        self.val = _val
        
class Dequeue(object):

    def __init__(self):
        # do some intialize if necessary
        self.first, self.last = None, None
        

    # @param {int} item an integer
    # @return nothing
    def push_front(self, item):
        # Write yout code here
        if self.first:
            tmp = Node(item)
            self.first.prev = tmp
            tmp.next = self.first
            self.first = tmp
        else:
            self.first = Node(item)
            self.last = self.first

    # @param {int} item an integer
    # @return nothing
    def push_back(self, item):
        # Write yout code here
        if self.last:
            tmp = Node(item)
            self.last.next = tmp
            tmp.prev = self.last
            self.last = tmp
        else:
            self.first = Node(item)
            self.last = self.first

    # @return an integer
    def pop_front(self):
        # Write your code here
        if self.first:
            item = self.first.val
            self.first = self.first.next
            if self.first:
                self.first.prev = None
            else:
                self.last.prev = None
            return item
        return -12
        
    # @return an integer
    def pop_back(self):
        # Write your code here
        if self.last:
            item = self.last.val
            self.last = self.last.prev
            if self.last:
                self.last.next = None
            else:
                self.first = None
            return item
        return -12
