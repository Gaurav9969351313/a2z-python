import sys
import csv
import tweepy
import pypyodbc
import sys
import datetime
import time


##d = datetime.datetime.strptime("2013-1-25", '%Y-%m-%d')
##print (datetime.date.strftime(d, "%dd%mm%y"))

from collections import Counter
from aylienapiclient import textapi

if sys.version_info[0] < 3:
   input = raw_input

## Twitter credentials
consumer_key = "p7HUdPLlkKaqlPn6TzKkA"
consumer_secret = "R7I1LRuLY27EKjzulutov74lKB0FjqcI2DYRUmsu7DQ"
access_token = "14898655-TE9dXQLrzrNd0Zwf4zhK7koR5Ahqt40Ftt35Y2qY"
access_token_secret = "q1lSRDOguxQrfgeWWSJgnMHsO67bqTd5dTElBsyTM"

## AYLIEN credentials
application_id = "0ca089d7"
application_key = "741775d7f669f5fad9f56c5415166cda"

## set up an instance of Tweepy
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

## set up an instance of the AYLIEN Text API
client = textapi.Client(application_id, application_key)

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
i = 0
## search Twitter for something that interests you
while i < resultsData:
    query = resultsDatas[i][2]
    print(query)
    number = 10

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
       fieldnames=["Tweet", "Sentiment","Confidence"]
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
               'Sentiment': response['polarity'],
               'Confidence': response['polarity_confidence']
           })
           time.sleep(1)
           now = datetime.datetime.now()
           searchId = datetime.date.strftime(now, "%d%m%y%H%M")
           SQLCommand1 = ("insert into sentimentTag(scriptName, url,publishedDate,confidence,sentiment,nSearchId, sSource) VALUES(?,?,?,?,?,?,?)")
           Values = [resultsDatas[i][2],response['text'],'25032018',response['polarity_confidence'],response['polarity'],searchId,'Twitter']
           cursor.execute(SQLCommand1, Values)
           connection.commit() 
          

           print("Analyzed Tweet {}".format(c))
          
    i+=1
connection.close()
print("gdf")
time.sleep(5)
