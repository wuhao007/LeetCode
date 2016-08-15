import Queue
class Solution(object):
    def findLadders(self, beginWord, endWord, wordlist):
        """
        :type beginWord: str
        :type endWord: str
        :type wordlist: Set[str]
        :rtype: List[List[int]]
        """
        if len(wordlist) == 0:
            return []
        mp = {}
        mn = sys.maxint
        queue = Queue.Queue()
        queue.put(endWord)
        ladder = {string: sys.maxint for string in wordlist}
        ladder[endWord] = 0
        wordlist.add(endWord)
        while not queue.empty():
            word = queue.get()
            step = ladder[word] + 1
            if step > mn:
                break
            for i in range(len(word)):
                for ch in string.ascii_lowercase:
                    new_word = word[:i] + ch + word[i+1:]
                    if new_word in ladder:
                        if step > ladder[new_word]:
                            continue
                        elif step < ladder[new_word]:
                            queue.put(new_word)
                            ladder[new_word] = step
            
                        if new_word in mp:
                            mp[new_word].append(word)
                        else:
                            mp[new_word] = [word]

                        if new_word == beginWord:
                            min = step
        result = []
        self.backTrace(beginWord, endWord, [], mp, result)
        return result
    def backTrace(self, word, end, lst, mp, result):
        if word == end:
            lst.append(end)
            result.append(lst[:])
            lst.pop()
            return
                           
        lst.append(word)
        if word in mp:
            for s in mp[word]:
                self.backTrace(s, end, lst, mp, result)
        lst.pop()
