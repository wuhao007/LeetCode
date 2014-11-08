class Solution:
    # @param start, a string
    # @param end, a string
    # @param dict, a set of string
    # @return a list of lists of string
    def getEntry(self, word, index):
        return word[:index] + word[index + 1:]
        
    def buildIndexes(self, length, dict):
        self.indexes = []
        for i in range(length):
            index = {}
            for word in dict:
                entry = self.getEntry(word, i)
                if entry in index:
                    index[entry] += [word]
                else:
                    index[entry] = [word]
            self.indexes += [index]

    def BFS(self, start, end):
        self.distance = {}
        self.distance[start] = 0
        queue = [start]
        while len(queue) != 0:
            head = queue.pop(0)
            level = self.distance[head] + 1
            for word in self.getNextWord(head):
                if word not in self.distance:
                    self.distance[word] = level
                    queue += [word]
    
    def DFS(self, curt, target, path):
        if curt == target:
            self.results += [path[:]]
        else:
            for word in self.getNextWord(curt):
                if word in self.distance and self.distance[word] + 1 == self.distance[curt]:
                    path += [word]
                    self.DFS(word, target, path)
                    path.pop()
                
    def getNextWord(self, word):
        for i in range(len(word)):
            entry = self.getEntry(word, i)
            if entry in self.indexes[i]:
                for nextWord in self.indexes[i][entry]:
                    if nextWord != word:
                        yield nextWord
                    
    def findLadders(self, start, end, dict):
        if start is None or end is None or len(start) != len(end):
            return []
            
        self.buildIndexes(len(start), dict)
        self.BFS(end, start)
        
        self.results = []
        if start in self.distance:
            self.DFS(start, end, [start])
        return self.results
