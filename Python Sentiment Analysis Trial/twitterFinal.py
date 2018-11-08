##WORKING

##from aylienapiclient import textapi
##
##client = textapi.Client("0ca089d7", "741775d7f669f5fad9f56c5415166cda")
##
##sentiment = client.Sentiment({'url': 'https://www.moneycontrol.com/news/business/indias-growth-engine-picks-pace-gdp-expands-8-2-in-\
##                                     june-quarter-highest-in-two-years-2904041.html'})
##print(sentiment['polarity'], sentiment['polarity_confidence'])
import sys
import tweepy
import pypyodbc
import datetime
import time

## collecting from db

connection = pypyodbc.connect('Driver={SQL Server};'
                              'Server=172.31.7.7;'
                                'Database=FT_IFTTT;'
                                'uid=odin;pwd=odin')
cursor = connection.cursor()

SQLCommand = ("SELECT * from tbl_AppletDetails where sStatus = 'Pending'")
cursor.execute(SQLCommand)
resultsDatas = cursor.fetchall()
resultsData = len(resultsDatas)
print(len(resultsDatas))

## search Twitter for something that interests you
i = 0
while i < resultsData:
    query = resultsDatas[i][2]
    print(query)
    i+=1


    ##WORKING

from newsapi import NewsApiClient

    # Init
newsapi = NewsApiClient(api_key='31f7c625c967479087b3472e0481ec30')

# /v2/get-everything
get_everything = newsapi.get_everything(q=query,sources='google-news-in',language='en')
print(len(get_everything))

articlesFinal = get_everything['articles'][1]
print(articlesFinal)
urlForSentiment = articlesFinal['url']

    ## API CALL for sentiment

from aylienapiclient import textapi

client = textapi.Client("0ca089d7", "741775d7f669f5fad9f56c5415166cda")

sentiment = client.Sentiment({'url': urlForSentiment})
print(sentiment['polarity'], sentiment['polarity_confidence'])

print(sentiment)


