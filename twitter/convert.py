"""
pass
"""

import pytz
from tweepy.tweet import Tweet

class TweetConvert:
    """
    pass
    """
    def __init__(self):
        self.tweet_list = None
        self.pre_tweet_list =[]

    def convert_to_telegram(self, tweet_list:list[Tweet]):
        '''
        Convert tweet information to the format sent to a telegram
        '''
        if len(tweet_list) == 0:
            return []
        self.tweet_list = tweet_list
        result = []
        for tweet in self.tweet_list:
            created_at = tweet.created_at
            #convert to beijing time
            beijing_time = created_at.astimezone(pytz.timezone('Asia/Shanghai'))
            beijing_time_format = beijing_time.strftime("%Y-%m-%d %H:%M:%S")
            #url for click
            tweet_id = tweet.id
            tweet_url = "https://twitter.com/i/web/status/" + str(tweet_id)
            item_info = "[" + beijing_time_format + "](" + tweet_url + ")"
            result.append(item_info)
        print("转换成功")
        return result

    def filter(self, tweet_list: list[Tweet]):
        """
        Filter out messages that have already been sent
        """
        if not tweet_list:
            return []
        result = []
        cur_tweet_list = []
        for tweet_info in tweet_list:
            if tweet_info.id not in self.pre_tweet_list:
                result.append(tweet_info)
            cur_tweet_list.append(tweet_info.id)
        #Store this ID list as pre_tweet_list for the next tweet_list
        self.pre_tweet_list = cur_tweet_list
        result.reverse()
        return result
