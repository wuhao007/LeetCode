class TrieNode:
  def __init__(self):
    # Initialize your data structure here.
    self.children = dict()
    self.isWord = False

class Trie:
  def __init__(self):
    self.root = TrieNode()

  # @param {string} word
  # @return {void}
  # Inserts a word into the trie.
  def insert(self, word):
    node = self.root
    for letter in word:
      child = node.children.get(letter)
      if child is None:
        child = TrieNode()
        node.children[letter] = child
      node = child
    node.isWord = True

  # @param {string} word
  # @return {boolean}
  # Returns if the word is in the trie.
  def search(self, word):
    node = self.root
    for letter in word:
      node = node.children.get(letter)
      if node is None:
        return False
    return node.isWord

  # @param {string} prefix
  # @return {boolean}
  # Returns if there is any word in the trie
  # that starts with the given prefix.
  def startsWith(self, prefix):
    node = self.root
    for letter in prefix:
      node = node.children.get(letter)
      if node is None:
        return False
    return True
