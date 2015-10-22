class Solution(object):
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        lst = []
        n = len(words)
        i = 0
        while i < n:
            ln = -1
            w = i
            while w < n and (ln + len(words[w]) + 1) <= maxWidth:
                ln += (len(words[w]) + 1)
                w += 1
            strBuilder = [words[i]]
            space = 1
            extra = 0
            if w != i + 1 and w != n:
                space = (maxWidth - ln) / (w - i - 1) + 1
                extra = (maxWidth - ln) % (w - i - 1)
            for j in range(i + 1, w):
                strBuilder += [' ' * space]
                if extra > 0:
                    strBuilder += [' ']
                    extra -= 1
                strBuilder += [words[j]]
            print strBuilder
            print len(strBuilder)
            strBuilder += [' ' * (maxWidth - len(strBuilder))]
            print strBuilder
            lst += [''.join(strBuilder)]
            i = w
        return lst
solution = Solution()
print solution.fullJustify([""], 2)

