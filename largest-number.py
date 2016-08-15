class Solution:
    # @param {integer[]} nums
    # @return {string}
    def largestNumber(self, nums):
        if num == None or len(num) == 0:
            return ''
        Snum = map(lambda x: str(x), nums)
        Snum.sort(cmp = lambda x, y: cmp(x+y, y+x))
        if Snum[-1][0] == '0':
            return '0'
        return ''.join(Snum[::-1])
        
                    
