import bisect
class RateLimiter:

    def __init__(self):
        # do some intialize if necessary
        self.mp = {}

    # @param {int} timestamp the current timestamp
    # @param {string} event the string to distinct different event
    # @param {string} rate the format is [integer]/[s/m/h/d]
    # @param {boolean} increment whether we should increase the counter
    # @return {boolean} true or false to indicate the event is limited or not
    def is_ratelimited(self, timestamp, event, rate, increment):
        # Write your code here
        start = rate.find("/")
        total_time = int(rate[:start])
        type = rate[start+1:]

        time = 1
        if type == 'm':
            time *= 60
        elif type == 'h':
            time = time * 60 * 60
        elif type == 'd':
            time = time * 60 * 60 * 24
        last_time = timestamp - time + 1

        if event not in self.mp:
            self.mp[event] = []

        rt = self.find_event(self.mp[event], last_time) >= total_time
        if increment and not rt:
            self.insert_event(self.mp[event], timestamp)

        return rt

    def insert_event(self, event, timestamp):
        event.append(timestamp)

    def find_event(self, event, last_time):
        ans = bisect.bisect_left(event, last_time)
        return len(event) - ans
