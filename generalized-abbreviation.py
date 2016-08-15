class Solution(object):
    def generateAbbreviations(self, word):
        """
        :type word: str
        :rtype: List[str]
        """
        ret = []
        self.backtrack(ret, word, 0, "", 0)
        return ret
    def backtrack(self, ret, word, pos, cur, count):
        if pos == len(word):
            if count > 0:
                cur += str(count)
                ret.append(cur)
        else:
            self.backtrack(ret, word, pos + 1, cur, count + 1)
            self.backtrack(ret, word, pos + 1, cur + str(count) if count > 0 else '' + word[pos], 0)
