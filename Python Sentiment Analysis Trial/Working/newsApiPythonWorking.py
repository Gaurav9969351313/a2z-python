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
import json
from newsapi import NewsApiClient
## collecting from db

connection = pypyodbc.connect('Driver={SQL Server};'
                              'Server=localhost;'
                                'Database=SentiMenti;'
                                'uid=odin;pwd=odin')
cursor = connection.cursor()

SQLCommand = ("select * from token")
cursor.execute(SQLCommand)
resultsDatas = cursor.fetchall()
resultsData = len(resultsDatas)
##print(len(resultsDatas))

## search Twitter for something that interests you
i = 0
while i < resultsData:
    scriptName = resultsDatas[i][0]
    print(scriptName)

    ##############################################################
    ## News APi
    # Init
    newsapi = NewsApiClient(api_key='31f7c625c967479087b3472e0481ec30')

    # /v2/get-everything
    get_everything = newsapi.get_everything(q=scriptName,sources='google-news-in',language='en')
    ##    print(len(get_everything))
    totalNewsCount = get_everything['totalResults']
    j = 0
    while j < totalNewsCount:
        articlesFinal = get_everything['articles'][j]['url']
        publishedDate = get_everything['articles'][j]['publishedAt']
        print(articlesFinal)

        ## getting sentiment for each url

        from aylienapiclient import textapi
        client = textapi.Client("0ca089d7", "741775d7f669f5fad9f56c5415166cda")
        sentiment = client.Sentiment({'url': articlesFinal})
        sentimentPolarity = sentiment['polarity']
        confidencePolarity = sentiment['polarity_confidence']
        print(sentiment['polarity'], sentiment['polarity_confidence'])

        ## Inserting into SQL
        now = datetime.datetime.now()
        searchId = datetime.date.strftime(now, "%d%m%y%H%M")
        SQLCommand1 = ("insert into sentimentTag(scriptName,url,publishedDate,confidence,sentiment,nTrendWieghtage,nSearchId) VALUES(?,?,?,?,?,?,?)")
        Values = [scriptName,articlesFinal,publishedDate,confidencePolarity,sentimentPolarity,'0',searchId]
        cursor.execute(SQLCommand1, Values)
        connection.commit()

        j+=1

    ##############################################################

    i+=1

