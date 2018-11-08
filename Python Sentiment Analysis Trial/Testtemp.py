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

## get data to ms sql

connection = pypyodbc.connect('Driver={SQL Server};Server=localhost;Database=SentiMenti;uid=odin;pwd=odin')

cursor = connection.cursor()
SQLCommand = 'SELECT * from token'
cursor.execute(SQLCommand)
results = cursor.fetchall()

## query = results[2][0]
totalTokens = len(results)
i = 0
while i < totalTokens:
    results[i][0]
    print(i)
    query = results[i][0]
    print (query)
    number = '1'

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

    # # AYLIEN API

    result = api.search(lang='en', q=query +' -rt', count=number,result_type='recent')
    print ('--- Gathered Tweets \n')
    
    i+=1
