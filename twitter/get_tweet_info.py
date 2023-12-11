"""
pass
"""
import tweepy
import conf

class Tweet:
    """
    pass
    """

    def __init__(self, bear_token:str):
        self.bear_token = bear_token
        self.client = tweepy.Client(self.bear_token)
        self.list_id = None

    def get_tweet_of_list(self, list_id=None, latest_id=None):
        """
        pass
        """
        if list_id is None:
            self.list_id = conf.TWEET_LIST_ID
        else:
            self.list_id = list_id

        circle = 0
        max_results = conf.MAX_RESULTS
        while True:
            tweet_fields = ['author_id','created_at','id','text','note_tweet']
            #resp = Response(data, includes, errors, meta)
            print(circle)
            resp = self.client.get_list_tweets(id=self.list_id,
                                               max_results=max_results+conf.CIRCLE_ADD*circle,
                                               tweet_fields=tweet_fields)
            if latest_id == 0 or latest_id is None:
                print("获取成功")
                return (resp.data[0].id,resp.data)

            trunc = -1
            for index,tweet in enumerate(resp.data):
                if latest_id == tweet.id:
                    trunc = index
                    break
            if trunc > -1:
                print("获取成功")
                return (resp.data[0].id, resp.data[:trunc])
            circle = circle + 1

    def get_token(self):
        '''
        pass
        '''
        return self.bear_token

    def get_token_laststr(self):
        """
        pass
        """
        return self.bear_token[-5:]
