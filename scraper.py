# -*- coding: utf-8 -*-
import sys
from bs4 import BeautifulSoup
from splinter import Browser
import urllib
import time

reload(sys)  # Reload does the trick!
sys.setdefaultencoding('UTF8')

if __name__ == '__main__':

    url = "http://data.gov.tw/node/7264"
    html = urllib.urlopen(url)
    soup = BeautifulSoup(html, "lxml")
    print soup.prettify()



'''
*+*+*+*+*+* REQUIREMENTS *+*+*+*+*+*+*

-e git+http://github.com/openaustralia/scraperwiki-python.git@morph_defaults#egg=scraperwiki

lxml==3.4.4
cssselect==0.9.1
beautifulsoup4
python-dateutil
selenium
splinter>=0.7.3




*+*+*+*+*+* TOP *+*+*+*+*+*+

# -*- coding: utf-8 -*-
import sys
from datetime import datetime
import urllib
from bs4 import BeautifulSoup
import scraperwiki


def get_soup(url):
    html = urllib.urlopen(url)
    soup = BeautifulSoup(html, "lxml")
    return soup


def get_links(url):
    soup = get_soup(url)
    links = soup.find()
    return links

if __name__ == '__main__':

    todays_date = str(datetime.now())





*+*+*+*+* BROWSER *+*+*+*+*+

def get_browse_soup(browser):
    html = browser.html
    soup = BeautifulSoup(html, "lxml")
    return soup


def browse(url):                                                                                            # loads all tenders
    browser = Browser("phantomjs", service_args=['--ignore-ssl-errors=true', '--ssl-protocol=any'])
    browser.visit(portal)
    browser.find_by_id('lnkClearAll').first.click()
    time.sleep(3)
    return browser




*+*+*+*+*+*+*+ DATA *+*+*+*+*+*+

                data = {"tender_url": unicode(tender_url),
                        "country": unicode(country),
                        "todays_date": todays_date}
                scraperwiki.sqlite.save(unique_keys=['tender_url'], data=data)


'''
