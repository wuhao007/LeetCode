"""
Definition of Column:
class Column:
    def __init__(self, key, value):
        self.key = key
        self.value = value
"""
from collections import OrderedDict

class MiniCassandra:

    def __init__(self):
        # initialize your data structure here.
        self.hash = {}

    # @param {string} raw_key a string
    # @param {int} column_key an integer
    # @param {string} column_value a string
    # @return nothing
    def insert(self, raw_key, column_key, column_value):
        # Write your code here
        if raw_key not in self.hash:
            self.hash[raw_key] = OrderedDict()
        self.hash[raw_key][column_key] = column_value


    # @param {string} raw_key a string
    # @param {int} column_start an integer
    # @param {int} column_end an integer
    # @return {Column[]} a list of Columns
    def query(self, raw_key, column_start, column_end):
        # Write your code here
        rt = []
        if raw_key not in self.hash:
            return rt

        self.hash[raw_key] = OrderedDict(sorted(self.hash[raw_key].items()))
        for key, value in self.hash[raw_key].items():
            if column_start <= key <= column_end:
                rt.append(Column(key, value))

        return rt
