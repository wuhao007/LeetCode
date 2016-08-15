class TwoSum(object):

    def __init__(self):
        """
        initialize your data structure here
        """
        self.table = {}

    def add(self, number):
        """
        Add the number to an internal data structure.
        :rtype: nothing
        """
        self.table[number] = self.table.get(number, 0) + 1
        

    def find(self, value):
        """
        Find if there exists any pair of numbers which sum is equal to the value.
        :type value: int
        :rtype: bool
        """
        for i in self.table.keys():
            j = value - i
            if i == j and self.table[i] > 1 or i != j and j in self.table:
                return True
        return False

# Your TwoSum object will be instantiated and called as such:
# twoSum = TwoSum()
# twoSum.add(number)
# twoSum.find(value)
