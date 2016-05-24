class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        n, cnt = len(s), len(words)
        if n <= 0 or cnt <= 0:
            return []
        mp = {}
        for word in words:
            if word in mp:
                mp[word] += 1
            else:
                mp[word] = 1
        ans = []
        wl = len(words[0])
        for i in range(wl):
            left = i
            count = 0
            tdict = {}
            for j in range(i, n - wl - 1):
                string = s[j:j + wl]
                if string in mp:
                    tdict[string] += 1
                    if tdict[string] <= mp[string]:
                        count += 1
                    else:
                        while tdict[string] > mp[string]:
                            str1 = s[left:left + wl]
                            tdict[str1] -= 1
                            if tdict[str1] < mp[str1]:
                                count -= 1
                            left += wl

                    if count = cnt:
                        ans.append(left)
                        tdict[s[left:left + wl]] -= 1
                        count -= 1
                        left += wl
                else:
                    tdict.clear()
                    count = 0
                    left = j + wl
        return ans            
                         
                        
                
        
