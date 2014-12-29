class Solution:
    # @return a tuple, (index1, index2)
    def twoSum(self, num, target):
        hash_map = {}
        for i in range(len(num)):
            if num[i] in hash_map:
                hash_map[num[i]] += [i]
            else:
                hash_map[num[i]] = [i]
        for key in hash_map:
            first = hash_map[key].pop(0)
            left = target - key
            if left in hash_map and len(hash_map[left]) > 0 and first < hash_map[left][-1]:
                return (first, hash_map[left].pop())
        return ()
