

from twx.botapi import TelegramBot, ReplyKeyboardMarkup
from TwitterAPI import TwitterAPI
from nsetools import Nse
from pprint import pprint


TWEET_TEXT = "||Shree Swami Samartha||"
CONSUMER_KEY = 'iAi9l9dLvBzKinhUdFJQ2dHaa'
CONSUMER_SECRET = 'eMBJTCjSKxd8tzHrmDLqB4yMtmleQSoXE6V1I2SP8YKAdUdP8N'
ACCESS_TOKEN_KEY = '3235720159-kYyjk5TbiB4BYjIgdRwiEmLM2NzZvqXL3UjsKuj'
ACCESS_TOKEN_SECRET = 'HtAD0ZNIJCe850y2KcUESMtfM8hrtQYSbwJZm6dI8ROGp'


api = TwitterAPI(CONSUMER_KEY,
                 CONSUMER_SECRET,
                 ACCESS_TOKEN_KEY,
                 ACCESS_TOKEN_SECRET)


nse = Nse()
q = nse.get_quote('infy')

#pprint(q)

str1 = str(q)

r = api.request('statuses/update', {'status': TWEET_TEXT})

print('SUCCESS' if r.status_code == 200 else 'FAILURE')

"""
Setup the bot
"""

bot = TelegramBot('332101015:AAFy9vC_d4Dj5GK7bkIQa5kETnudMqZWUhY')
bot.update_bot_info().wait()
print(bot.username)

"""
Send a message to a user
"""
user_id = int(185350524)

result = bot.send_message(user_id, str1).wait()
print(result)

"""
Get updates sent to the bot
"""
updates = bot.get_updates().wait()
for update in updates:
    print(update)

"""
Use a custom keyboard
"""
keyboard = [
    ['7', '8', '9'],
    ['4', '5', '6'],
    ['1', '2', '3'],
         ['0']
]
reply_markup = ReplyKeyboardMarkup.create(keyboard)

bot.send_message(user_id, 'please enter a number', reply_markup=reply_markup).wait()

print reply_markup



