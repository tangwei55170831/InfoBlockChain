"""
pass
"""
import os
import time
import json
from dotenv import load_dotenv
from twitter.get_tweet_info import Tweet
from twitter.convert import TweetConvert
from telegram.bot import Telegram

import conf

def main():
    '''
    pass
    '''
    #sleep a few mins when system start up
    time.sleep(conf.START_UP_TIME)
    error_time = 0
    error_message = ""
    telegram = Telegram()
    tweet_list = []
    tweet_token_list = json.loads(os.getenv("BEARER_TOKEN_LIST"))
    telegram_token_list = json.loads(os.getenv("TELEGRAM_TOKEN_LIST"))
    tweet_num = len(tweet_token_list)
    for tweet_token in tweet_token_list:
        tweet_list.append(Tweet(tweet_token))

    tweet_convert = TweetConvert()
    times = 0
    latest_id = 0
    while True:
        times = times + 1
        print("第"+str(times)+"次")

        object_index = (times//conf.TRUN_TIME)%tweet_num

        try:
            request_tweet = tweet_list[object_index]
            latest_id,tweets_result = request_tweet.get_tweet_of_list(latest_id = latest_id)
        except Exception as e:
            #When an exception is raised, call a different token
            times = times + conf.TRUN_TIME
            error_message = repr(e)
            error_time = error_time + 1
        else:
            error_time = 0

        if error_time > 0:
            message = f"[ERROR]:\n   \
            [TOKEN]{request_tweet.get_token_laststr()} \n   \
            [MESSAGE]: {error_message}"
            telegram.send_massages_to_chat(message,telegram_token_list[0])
        if error_time == tweet_num:
            time.sleep(15*60)
            error_time = 0

        tweets_result.reverse()

        convert_info_list = tweet_convert.convert_to_telegram(tweets_result)

        telegram.multi_send(convert_info_list,telegram_token_list)

        time.sleep(conf.INTERVAL)

if __name__ == "__main__":
    load_dotenv(verbose=True)
    main()
