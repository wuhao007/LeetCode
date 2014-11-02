class Solution:
    # @param words, a list of strings
    # @param L, an integer
    # @return a list of strings
    def fullJustify(self, words, L):
        if words == []:
            return []
        sum_words = len(words[0])
        row = [words[0]]
        k = 0
        for i in range(1,len(words)):
            if sum_words + 1 + len(words[i]) <= L:
                sum_words += (1 + len(words[i]))
                row += [words[i]]
                k = i
            else:
                break
        num_break = len(row) - 1
        if k + 1 == len(words):
            last_str = ' '.join(row)
            return [last_str + ' '*(L - len(last_str))]
        if num_break > 0:
            num_space = L - sum_words
            div_space = num_space / num_break
            mod_space = num_space - div_space * num_break
            row_str = row[0]
            for i in range(1, len(row)):
                if mod_space > 0:
                    row_str += (' '*(div_space+2) + row[i])
                    mod_space -= 1
                else:
                    row_str += (' '*(div_space+1) + row[i])
            return [row_str] + self.fullJustify(words[k+1:], L)
        else:
            return [row[0] + ' '*(L - len(row[0]))] + self.fullJustify(words[1:], L)

        
solution = Solution()
print solution.fullJustify(["What","must","be","shall","be."], 12)

