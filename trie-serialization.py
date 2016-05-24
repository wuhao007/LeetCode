class Solution:

    '''
    @param root: An object of TrieNode, denote the root of the trie.
    This method will be invoked first, you should design your own algorithm 
    to serialize a trie which denote by a root node to a string which
    can be easily deserialized by your own "deserialize" method later.
    '''
    def serialize(self, root):
        # Write your code here
        if root is None:
            return ""

        data = ""
        for key, value in root.children.items():
            data += key + self.serialize(value)

        return "<%s>" % data


    '''
    @param data: A string serialized by your serialize method.
    This method will be invoked second, the argument data is what exactly
    you serialized at method "serialize", that means the data is not given by
    system, it's given by your own serialize method. So the format of data is
    designed by yourself, and deserialize it here as you serialize it in 
    "serialize" method.
    '''
    def deserialize(self, data):
        # Write your code here
        if data is None or len(data) == 0:
            return None

        root = TrieNode()
        current = root
        path = []
        for c in data:
            if c == '<':
                path.append(current)
            elif c == '>':
                path.pop()
            else:
                current = TrieNode()
                path[-1].children[c] = current

        return root
