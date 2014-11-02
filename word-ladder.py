class Solution:
    # @param start, a string
    # @param end, a string
    # @param dict, a set of string
    # @return an integer
    def ladderLength(self, start, end, dict):
        queue = [(start, 1)]
        n = len(start)
        indexes = [{} for _ in range(n)]
        for word in dict:
            for i in range(n):
                sub_word = word[:i] + word[i+1:]
                if sub_word in indexes[i]:
                    indexes[i][sub_word] += [word]
                else:
                    indexes[i][sub_word] = [word]
        while len(queue) > 0:
            node, level = queue.pop(0)
            for i in range(n):
                sub_word = node[:i] + node[i+1:]
                if end.find(sub_word) != -1:
                    return level + 1
                elif sub_word in indexes[i]:
                    for word in indexes[i][sub_word]:
                        if word != node:
                            queue += [(word, level + 1)]
        return 0

solution = Solution()
print solution.ladderLength('hit', 'cog', ["hot","dot","dog","lot","log"])
print solution.ladderLength("hot", "dog", ["hot","dog"])
