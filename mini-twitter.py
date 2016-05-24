'''
Definition of Tweet:
class Tweet:
    @classmethod
    def create(cls, user_id, tweet_text):
         # This will create a new tweet object,
         # and auto fill id
'''
class MiniTwitter:

    def __init__(self):
        # initialize your data structure here.
        self.order = 0
        self.users_tweets = {}
        self.friends = {}

    # @param {int} user_id
    # @param {str} tweet
    # @return {Tweet} a tweet
    def postTweet(self, user_id, tweet_text):
        # Write your code here
        tweet = Tweet.create(user_id, tweet_text)
        self.order += 1
        if user_id in self.users_tweets:
            self.users_tweets[user_id].append((self.order, tweet))
        else:
            self.users_tweets[user_id] = [(self.order, tweet)]
        return tweet

    # @param {int} user_id
    # return {Tweet[]} 10 new feeds recently
    # and sort by timeline
    def getNewsFeed(self, user_id):
        # Write your code here
        rt = []
        if user_id in self.users_tweets:
            rt = self.users_tweets[user_id][-10:]

        if user_id in self.friends:
            for friend in self.friends[user_id].keys():
                if friend in self.users_tweets:
                    rt.extend(self.users_tweets[friend][-10:])

        rt.sort(cmp=lambda x, y : cmp(x[0], y[0]))
        return [tweet[1] for tweet in rt[-10:][::-1]]
        
    # @param {int} user_id
    # return {Tweet[]} 10 new posts recently
    # and sort by timeline
    def getTimeline(self, user_id):
        # Write your code here
        if user_id in self.users_tweets:
            return [tweet[1] for tweet in self.users_tweets[user_id][-10:][::-1]]
        else:
            return []

    # @param {int} from user_id
    # @param {int} to_user_id
    # from user_id follows to_user_id
    def follow(self, from_user_id, to_user_id):
        # Write your code here
        if from_user_id not in self.friends:
            self.friends[from_user_id] = set()
        self.friends[from_user_id].add(to_user_id)

    # @param {int} from user_id
    # @param {int} to_user_id
    # from user_id unfollows to_user_id
    def unfollow(self, from_user_id, to_user_id):
        # Write your code here
        if from_user_id not in self.friends:
            return
        if to_user_id not in self.friends[from_user_id]:
            return
        del self.friends[from_user_id].remove(to_user_id)
