


from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
from pprint import pprint

#consumer key, consumer secret, access token, access secret.
ckey="A0F7ath6BW1zAl3Tpg8YHHiPF"
csecret="Ua2YJed9vo55Zr0wSLfXiFTD7nOnf6IvpLG1TFPexzuCsHcG1x"
atoken="3235720159-kYyjk5TbiB4BYjIgdRwiEmLM2NzZvqXL3UjsKuj"
asecret="HtAD0ZNIJCe850y2KcUESMtfM8hrtQYSbwJZm6dI8ROGp"

class listener(StreamListener):

    def on_data(self, data):
        pprint(data)
        return(True)

    def on_error(self, status):
        print status

auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)

twitterStream = Stream(auth, listener())
twitterStream.filter(track=["software"])
