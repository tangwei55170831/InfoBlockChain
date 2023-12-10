"""
pass
"""
import os
import time
from dotenv import load_dotenv

from twitter.getTweetInfo import Tweet
from twitter.convert import TweetConvert
from telegram.bot import Telegram

import conf

def main():
    '''
    pass
    '''
    #sleep a few mins when system start up
    time.sleep(conf.START_UP_TIME)
    telegram = Telegram()
    tweet = Tweet(os.getenv("BEARER_TOKEN"))
    tweet_convert = TweetConvert()
    times = 0
    while True:
        times = times + 1
        print("第"+str(times)+"次")
        tweets_result = tweet.get_tweet_of_list()

        filter_sent_result = tweet_convert.filter(tweets_result)

        convert_info_list = tweet_convert.convert_to_telegram(filter_sent_result)

        telegram.multi_send(convert_info_list)


        time.sleep(conf.INTERVAL)
if __name__ == "__main__":
    load_dotenv(verbose=True)
    main()
