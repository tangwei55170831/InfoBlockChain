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
