# The read4 API is already defined for you.
# @param buf, a list of characters
# @return an integer
# def read4(buf):

class Solution(object):
    buffPtr = 0
    buffCnt = 0
    buff = [''] * 4
    def read(self, buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Maximum number of characters to read (int)
        :rtype: The number of characters read (int)
        """
        ptr = 0
        while ptr < n:
            if self.buffPtr == 0:
                self.buffCnt = read4(self.buff)
            if self.buffCnt == 0:
                break
            while ptr < n and self.buffPtr < self.buffCnt:
                buf[ptr] = self.buff[self.buffPtr]
                ptr += 1
                self.buffPtr += 1
            if self.buffPtr >= self.buffCnt:
                self.buffPtr = 0
        return ptr
                
