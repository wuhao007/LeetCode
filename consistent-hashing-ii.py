class Solution:

    # @param {int} n a positive integer
    # @param {int} k a positive integer
    # @return {Solution} a Solution object
    @classmethod
    def create(cls, n, k):
        # Write your code here
        solution = cls()
        solution.ids = {}
        solution.machines = {}
        solution.n = n
        solution.k = k
        return solution

    # @param {int} machine_id an integer
    # @return {int[]} a list of shard ids
    def addMachine(self, machine_id):
        # write your code here
        ids = []
        import random
        for i in xrange(self.k):
            index = random.randint(0, self.n - 1)
            while index in self.ids:
                index = random.randint(0, self.n - 1)

            ids.append(index)
            self.ids[index] = True

        ids.sort()
        self.machines[machine_id] = ids
        return ids

    # @param {int} hashcode an integer
    # @return {int} a machine id
    def getMachineIdByHashCode(self, hashcode):
        # write your code here
        machine_id = -1
        distance = self.n + 1

        for key, value in self.machines.items():
            import bisect
            index = bisect.bisect_left(value, hashcode) % len(value)
            d = value[index] - hashcode
            if d < 0:
                d += self.n

            if d < distance:
                distance = d
                machine_id = key

        return machine_id
