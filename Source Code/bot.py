#!/usr/bin/env python3

import requests
import json
import configparser as cfg

class Tele_bot():
    def __init__(self, config):
        self.token = self.read_token_from_config_file(config)
        self.base = "https://api.telegram.org/bot{}/".format(self.token)

    def get_updates(self, offset = None):
        url = self.base + "getupdates?timeout=100"
        if offset:
            url = url + "&offset={}".format(offset+1)
        response = requests.get(url)
        return json.loads(response.content)
    
    def send_message(self, msg, chat_id):
        url = self.base + "sendMessage?chat_id={}&text={}".format(chat_id, msg)
        if msg is not None:
            requests.get(url)
    
    def read_token_from_config_file(self, config):
        parser = cfg.ConfigParser()
        parser.read(config)
        return parser.get('creds', 'token')
