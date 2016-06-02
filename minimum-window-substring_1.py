class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        mp = [0] * 128
        for c in t:
            mp[ord(t)] += 1
        counter = len(t)
        begin, end = 0, 0
        d = sys.maxint
        head = 0
        while end < len(s):
            c = s[end] 
            end += 1
            if mp[c] > 0:
                mp[c] -= 1
                counter -= 1
            while counter == 0:
                if end - begin < d:
                    d, head = end - head, begin
                if mp[s[begin]] == 0:
                    begin += 1
                    counter += 1
        return '' if d == sys.maxint else s[head:head+d]

