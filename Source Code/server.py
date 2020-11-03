#!/usr/bin/env python3

import random
from bot import Tele_bot

bot = Tele_bot("config.cfg")

def make_reply(msg):
    greeting = ["ay", "ayy", "aye", "hi", "hai", "hy", "hyy","hyyy", "hey", "hlo", "hello"]
    if msg.lower() in greeting:
        return random.choice(greeting).capitalize()
    return random.choice(["You're Awesome.", "You are one in a Million!", "You can do it!",
    "Try and Fail. But, Never Try to Fail.", "This is Your Day"])

update_id = None

while True:
    updates = bot.get_updates(offset=update_id)
    updates = updates["result"]
    if updates:
        for item in updates:
            update_id = item["update_id"]
            try:
                message = item["message"]["text"]
            except:
                message = None
            
            to = item["message"]["from"]["id"]
            reply = make_reply(message)
            bot.send_message(reply, to)
