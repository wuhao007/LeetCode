# The read4 API is already defined for you.
# @param buf, a list of characters
# @return an integer
# def read4(buf):

class Solution(object):
    def read(self, buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Maximum number of characters to read (int)
        :rtype: The number of characters read (int)
        """
        eof = False
        total = 0
        tmp = [''] * 4
        while not eof and total < n:
            count = read4(tmp)
            eof = count < 4
            count = min(count, n - total)
            for i in range(count):
                buf[total] = tmp[i]
                total += 1
        return total

        
