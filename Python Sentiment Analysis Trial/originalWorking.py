#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import csv
import tweepy
import datetime
import pypyodbc
import sys
from collections import Counter
from aylienapiclient import textapi
now = datetime.datetime.now()

if sys.version_info[0] < 3:
    input = raw_input


## SQL Connection
    
connection = pypyodbc.connect('Driver={SQL Server};'
                              'Server=localhost;'
                                'Database=SentiMenti;'
                                'uid=odin;pwd=odin')
cursor = connection.cursor()

    ## Twitter credentials

consumer_key = 'p7HUdPLlkKaqlPn6TzKkA'
consumer_secret = 'R7I1LRuLY27EKjzulutov74lKB0FjqcI2DYRUmsu7DQ'
access_token = '14898655-TE9dXQLrzrNd0Zwf4zhK7koR5Ahqt40Ftt35Y2qY'
access_token_secret = 'q1lSRDOguxQrfgeWWSJgnMHsO67bqTd5dTElBsyTM'

    ## AYLIEN credentials

application_id = '0ca089d7'
application_key = '741775d7f669f5fad9f56c5415166cda'

## set up an instance of Tweepy
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

## set up an instance of the AYLIEN Text API
client = textapi.Client(application_id, application_key)

## search Twitter for something that interests you
query = input("What subject do you want to analyze for this example? \n")
number = input("How many Tweets do you want to analyze? \n")

results = api.search(
   lang="en",
   q=query + " -rt",
   count=number,
   result_type="recent"
)

print("--- Gathered Tweets \n")

## open a csv file to store the Tweets and their sentiment 
file_name = 'Sentiment_Analysis_of_{}_Tweets_About_{}.csv'.format(number, query)

with open(file_name, 'w', newline='') as csvfile:
   csv_writer = csv.DictWriter(
       f=csvfile,
       fieldnames=["Tweet", "Sentiment"]
   )
   csv_writer.writeheader()

   print("--- Opened a CSV file to store the results of your sentiment analysis... \n")

## tidy up the Tweets and send each to the AYLIEN Text API
   for c, result in enumerate(results, start=1):
       tweet = result.text
       tidy_tweet = tweet.strip().encode('ascii', 'ignore')

       if len(tweet) == 0:
           print('Empty Tweet')
           continue

       response = client.Sentiment({'text': tidy_tweet})
       csv_writer.writerow({
           'Tweet': response['text'],
           'Sentiment': response['polarity']
       })

       print("Analyzed Tweet {}".format(c))


SQLCommand = ("insert into sentimentTag(scriptName, url,publishedDate, confidence, sentiment) VALUES(?,?,?,?,?)")
Values = [Tweet,Sentiment,'cd',10,'cd']
cursor.execute(SQLCommand, Values)
connection.commit() 
connection.close()
