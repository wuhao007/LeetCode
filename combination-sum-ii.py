class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        res = []
        combination = []
        self.combinationSum(candidates, target, res, combination, 0)
        return res
    def combinationSum(self, candidates, target, res, combination, begin):
        if target = 0:
            res.append(combination[:])
            return
        for i in range(begin, len(candidates)):
            if target >= candidates[i]:
                if i == begin or candidates[i] != candidates[i - 1]:
                    combination.append(candidates[i])
                    self.combinationSum(candidates, target - candidates[i], res, combination, i + 1)
                    combination.pop()
            
