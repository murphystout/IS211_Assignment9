from bs4 import BeautifulSoup
import urllib2

url = "http://www.wunderground.com/history/airport/KNYC/2015/4/1/MonthlyCalendar.html"
page = urllib2.urlopen(url)
soup = BeautifulSoup(page.read())
datatable = None

tables = soup.find_all('table')
for table in tables:
	try:
		if table.get('class')[0]  == "calendar-history-table":
			datatable = table
	except:
		continue

tds = datatable.find_all('td',class_="day")
for td in tds:
	try:
		date = td.find_all('a',class_="dateText")[0]
		value_header = td.find_all('td',class_="value-header")[0]
		highlow = td.find_all('td',class_="values highLow")[0]
		

		print "Day: %s \t %s \t High|Low %s" % (date.get_text(), value_header.get_text(),highlow.get_text())
		
	except:
		continue
	

