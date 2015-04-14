from bs4 import BeautifulSoup
import urllib2
import csv

url = "http://finance.yahoo.com/q/hp?s=AAPL+Historical+Prices"
page = urllib2.urlopen(url)
soup = BeautifulSoup(page.read())
datatable = None
date = None
close = None
tables = soup.find_all('table')
for table in tables:
	tableclass = table.get('class')
	try:
		if (tableclass[0] == "yfnc_datamodoutline1"):
			datatable = table.find_all('table')[0]
	except:
		continue
trs = datatable.find_all('tr')
for tr in trs:
	try:
		tds = tr.find_all('td')
		date = str(tds[0].get_text())
		close = str(tds[4].get_text())
	except:
		continue
	print "Date: %s \t Close: %s" % (date,close)
	
	
	
	
		
	


