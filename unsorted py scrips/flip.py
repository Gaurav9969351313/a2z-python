import urllib2
from bs4 import BeautifulSoup
import requests

AMAZON_URL = "http://www.amazon.in/"

FLIPKART_URL = "http://www.flipkart.com/"

SEARCH_KEYWORD = raw_input("Enter the product name to compare :")

SEARCH_KEYWORD = SEARCH_KEYWORD.lower()

SPLITTED_KEYWORD = SEARCH_KEYWORD.split()

SEARCH_FLIPKART_URL = FLIPKART_URL + "searchq?" 

for i in range(len(SPLITTED_KEYWORD)):
	SEARCH_FLIPKART_URL = SEARCH_FLIPKART_URL + "+" + SPLITTED_KEYWORD[i]

def url_crawler(url):
	requester = urllib2.Request(url, headers={'User-Agent': "Magic Browser"})
	connector = urllib2.urlopen(requester)
	connector_reader = connector.read()
	soup = BeautifulSoup(connector_reader, "lxml")
	return soup

soup = url_crawler(SEARCH_FLIPKART_URL)

#print soup

product_class = soup.findAll("div", {"class": "gd-col gu3"})

print product_class

product_class_list = []

for div in product_class:
	print div
