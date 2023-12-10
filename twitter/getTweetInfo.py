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

    def get_tweet_of_list(self, list_id=None):
        """
        pass
        """
        if list_id is None:
            self.list_id = conf.TWEET_LIST_ID
        else:
            self.list_id = list_id

        #set parameters
        max_results = conf.MAX_RESULTS
        tweet_fields = ['author_id','created_at','id','text','note_tweet']
        #resp = Response(data, includes, errors, meta)
        resp = self.client.get_list_tweets(id=self.list_id,
                                           max_results=max_results,
                                           tweet_fields=tweet_fields)
        print("获取成功")
        return resp.data
