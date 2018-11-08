from TwitterAPI import TwitterAPI


TWEET_TEXT = "||Shree Swami Samartha||"


CONSUMER_KEY = 'iAi9l9dLvBzKinhUdFJQ2dHaa'
CONSUMER_SECRET = 'eMBJTCjSKxd8tzHrmDLqB4yMtmleQSoXE6V1I2SP8YKAdUdP8N'
ACCESS_TOKEN_KEY = '3235720159-kYyjk5TbiB4BYjIgdRwiEmLM2NzZvqXL3UjsKuj'
ACCESS_TOKEN_SECRET = 'HtAD0ZNIJCe850y2KcUESMtfM8hrtQYSbwJZm6dI8ROGp'


api = TwitterAPI(CONSUMER_KEY,
                 CONSUMER_SECRET,
                 ACCESS_TOKEN_KEY,
                 ACCESS_TOKEN_SECRET)

r = api.request('statuses/update', {'status': TWEET_TEXT})

print('SUCCESS' if r.status_code == 200 else 'FAILURE')
