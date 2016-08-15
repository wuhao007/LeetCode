class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: Set[str]
        :rtype: int
        """
        length = 2
        front, back = set([beginWord]), set([endWord])
        wordList.discard(beginWord)
        while front:
            front = wordList & (set(word[:index] + ch + word[index+1:] for word in front for index in range(len(beginWord)) for ch in string.ascii_lowercase))
            if front & back:
                return length
            length += 1
            if len(front) > len(back):
                front, back = back, front
            wordList -= front
        return 0
