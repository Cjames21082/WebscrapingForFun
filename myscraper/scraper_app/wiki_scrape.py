"""Packages used:
   * BeautifulSoup a library designed for screen-scraping HTML and XML
   	 documentation: http://www.crummy.com/software/BeautifulSoup/
   * Requests is a library to handle HTTP requests and responses
   	 documentation: http://docs.python-requests.org/en/latest/
   """
from bs4 import BeautifulSoup
import requests
import sys

""" Script to scrape wikipedia website and return genres of tv shows """

# request url from user
url = raw_input("Enter a Wikipedia URL to extract the genres(Enter 'q' to exit):")

# run search
while url != 'q':

	# error check: valid URL
	try:
		response = requests.get(url.strip())
	except:
		print "Invalid URL: %s" %url
		sys.exit(255)

	# error check: HTTP Client Error (i.e 'Page not Found'), HTTP Server Error
	if response.status_code in range(400,500):
		print "HTTP Client Error code %s" % response.status_code
		sys.exit(4)
	elif response.status_code in range(500,600):
		print "HTTP Server Error: code %s" % response.status_code
		sys.exit(5)

	# read url content
	data = response.text

	# use BeautifulSoup to locate tag holding genre information
	tvshow = BeautifulSoup(data)
	print "Genres: " + ", ".join(tvshow.find('td',{'class':"category"}).get_text().split('\n'))
	print "\n"

	# user can enter another wikipedia url
	url = raw_input("Enter another Wikipedia URL to extract the genres(Enter 'q' to exit):")

