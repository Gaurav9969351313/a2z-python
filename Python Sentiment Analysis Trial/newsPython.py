newsapi = NewsApiClient(api_key='31f7c625c967479087b3472e0481ec30')

    # /v2/get-everything
get_everything = newsapi.get_everything(q=query,sources='google-news-in',language='en')
    ##    print(len(get_everything))
print (get_everything)

articlesFinal = get_everything['articles'][1]
print(articlesFinal)
urlForSentiment = articlesFinal['publishedAt'][1]
print(urlForSentiment)

    ## API CALL for sentiment

from aylienapiclient import textapi

client = textapi.Client("0ca089d7", "741775d7f669f5fad9f56c5415166cda")

sentiment = client.Sentiment({'url': urlForSentiment})
print(sentiment['polarity'], sentiment['polarity_confidence'])

print(sentiment)
