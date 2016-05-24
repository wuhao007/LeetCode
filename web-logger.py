class WebLogger:
    
    def __init__(self):
        # initialize your data structure here.
        self.timestamps = []
        self.counter = 0

    # @param {int} timestamp an integer
    # @return nothing
    def hit(self, timestamp):
        # Write your code here
        self.counter += 1
        if len(self.timestamps) > 0 and self.timestamps[-1][0] == timestamp:
            self.timestamps[-1] = (self.timestamps[-1][0], self.timestamps[-1][1] + 1)
        else:
            self.timestamps.append((timestamp, 1))

    # @param {int} timestamp an integer
    # @return {int} an integer
    def get_hit_count_in_last_5_minutes(self, timestamp):
        # Write your code here
        while len(self.timestamps) > 0 and self.timestamps[0][0] + 300 <= timestamp:
            self.counter -= self.timestamps[0][1]
            self.timestamps.pop(0)

        return self.counter
