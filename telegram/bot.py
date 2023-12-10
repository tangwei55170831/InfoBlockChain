"""
pass
"""

import os
import time
import requests
import json

import conf

class Telegram:
    """
    pass
    """
    def __init__(self, chat_id=None):
        self.chat_id = chat_id
        if chat_id is not None:
            self.chat_id = chat_id
        else:
            self.chat_id = conf.CHAT_ID
        self.request_timeout = 10
        self.request_ok_list = [
            requests.codes['ok'],
            requests.codes['created'],
            requests.codes['no_content']]

    def send_massages_to_chat(self, text:str, token):
        """
        send massages to chat
        """
        send_url = f"https://api.telegram.org/bot{token}/sendMessage"
        payload = {
            'chat_id': self.chat_id,
            'text': text,
            'parse_mode': 'Markdown'
        }
        #send_url = send_url + rf"?chat_id={self.chat_id}" + rf"&text={text}"
        resp = requests.post(send_url, json=payload, timeout=self.request_timeout)
        if resp.status_code not in self.request_ok_list:
            raise ValueError("[ERROR]: send telegram error!")

        return resp

    def multi_send(self, text_list: list):
        """
        send info 20 messages per second
        """
        if len(text_list) == 0:
            print("No new messages!")
            return
        size = conf.CHUNK_SIZE
        text_list_20_per = [text_list[i:i + size] for i in range(0, len(text_list), size)]
        token_list = json.loads(os.getenv("TELEGRAM_TOKEN_LIST"))
        for index, text_list_20 in enumerate(text_list_20_per):
            for text in text_list_20:
                self.send_massages_to_chat(text, token_list[index])
            time.sleep(1)
        print("发送完成")
