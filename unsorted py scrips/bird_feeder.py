
from datetime import datetime
import serial
import sqlite3
import twitter
import os


if sys.platform == "win32":
    os.system("cls")
else:
    os.system("clear")


XBeePort = serial.Serial('/dev/tty.YOUR_SERIAL_DEVICE', \
baudrate = 9600, timeout = 1)

sqlconnection = sqlite3.connect("tweetingbirdfeeder.sqlite3")

sqlcursor = sqlconnection.cursor()



api = twitter.Api('Your_OAuth_Consumer_Key', 'Your_OAuth_Consumer_Secret', \
'Your_OAuth_Access_Token', 'Your_OAuth_Access_Token_Secret')


def transmit(msg):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    if msg == "arrived":
        tweet = "A bird has landed on the perch!"
        table = "birdfeeding"
    if msg == "departed":
        tweet = "A bird has left the perch!"
        table = "birdfeeding"
    if msg == "refill":
        tweet = "The feeder is empty."
        table = "seedstatus"
    if msg == "seedOK":
        tweet = "The feeder has been refilled with seed."
        table = "seedstatus"
    print "%s - %s" % (timestamp.strftime("%Y-%m-%d %H:%M:%S"), tweet)

try:
    sqlstatement = "INSERT INTO %s (id, time, event) \
VALUES(NULL, \"%s\", \"%s\")" % (table, timestamp, msg)
    sqlcursor.execute(sqlstatement)
    sqlconnection.commit()
except:
    print "Could not store event to the database."
pass


try:
    status = api.PostUpdate(msg)
except:
    print "Could not post Tweet to Twitter"
pass


# Main program loop
try:
    while 1:
    
# listen for inbound characters from the feeder-mounted XBee radio
        message = XBeePort.readline()

# Depending on the type of message is received,
# log and tweet it accordingly

        if "arrived" in message:
            transmit("arrived")
        if "departed" in message:
            transmit("departed")
        if "refill" in message:
            transmit("refill")
        if "seedOK" in message:
            transmit("seedOK")
except KeyboardInterrupt:
    
# Exit the program when the Control-C keyboard interrupt been detected
#print "Quitting the Tweeting Bird Feeder Listener Program."
    sqlcursor.close()
pass
