################################################
# Configure variables below for connecting to the SQL database
################################################
$CSVFileName = "C:\Users\Administrator\Desktop\Working'\Sentiment_Analysis_of_10_Tweets_About_sbi stock.csv"
$SQLInstance = "."
$SQLDatabase = "SentiMenti"
$SQLTable = "sentimentTag"

##############################################
# Prompting for SQL credentials
##############################################

$SQLUsername = 'odin'
$SQLPassword = 'odin'

##############################################
# Importing SqlServer module
##############################################
Import-Module SqlServer


##############################################
# Importing CSV and processing data
##############################################
$CSVImport = Import-CSV $CSVFileName
$CSVRowCount = $CSVImport.Count

##############################################
# ForEach CSV Line Inserting a row into the Temp SQL table
##############################################

ForEach ($CSVLine in $CSVImport)
{
# Setting variables for the CSV line, ADD ALL 170 possible CSV columns here
$CSVScrip = $CSVLine.Scrip
$CSVTweet = $CSVLine.Tweet
$CSVDate = $CSVLine.Date
$CSVConfidence = $CSVLine.Confidence
$CSVSentiment = $CSVLine.Sentiment

##############################################
# SQL INSERT of CSV Line/Row
##############################################
$SQLInsert = @"
INSERT INTO $SQLTable
VALUES ('$CSVScrip','$CSVTweet','$CSVDate','$CSVConfidence','$CSVSentiment')
"@
# Running the INSERT Query
Invoke-SQLCmd -Query $SQLInsert -ServerInstance $SQLInstance -Username $SQLUsername -Password $SQLPassword -Database $SQLDatabase
# End of ForEach CSV line below
}
