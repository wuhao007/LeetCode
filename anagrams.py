class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        if strs == None or len(strs) == 0:
            return []
        mp = {}
        strs.sort()
        for s in strs:
            keyStr = ''.join(sorted(s))
            if keyStr in mp:
                mp[keyStr].append(s)
            else:
                mp[keyStr] = []
        return mp.values()
