'''
NOTES

start time. 7.40 uk
suggest putting in 'original lang' boolean column
function for country code?
check buyer/name vs legalName
add currency column - currently in column header
check format of 'address' as schema split into street, locality, postcode etc
mmp_in delete exxtra colum header from typo - awarding_add
ungm_int :  sew together first name + last name, country codes + phone/fax


push bund_de  -  download csv - delete data to replace with eng cols
eservices_wor : separate return address into lines - contents
bad summary - due_north

'''








# -*- coding: utf-8 -*-
import sys
from bs4 import BeautifulSoup
from splinter import Browser
import time
import urllib
import requests
from datetime import datetime
import scraperwiki
import os

reload(sys)  # Reload does the trick!
sys.setdefaultencoding('UTF8')


def get_soup(url):
    html = urllib.urlopen(url)
    soup = BeautifulSoup(html, "lxml")
    return soup


def get_login(url):

    #browser = Browser("phantomjs", service_args=['--ignore-ssl-errors=true', '--ssl-protocol=any'])
    current_directory = os.path.dirname(os.path.abspath(__file__))
    driver_path = os.path.join(current_directory, 'chromedriver')
    print driver_path
    browser = Browser(driver_name='chrome', executable_path=driver_path)
    browser.visit(url)
    time.sleep(2)
    print browser.html

    browser.find_by_id('email').first.fill('j.black.services0@gmail.com')
    browser.find_by_id('password').first.fill('Nrjn1gsa')
    browser.find_by_value('Login').first.click()

    return browser


if __name__ == '__main__':

    todays_date = str(datetime.now())
    portal = "https://www.b2bquote.co.uk/"
    country_code = 'uk'

    browser = get_login(portal)













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
from splinter import Browser
import time
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
    country_code = ''
    errors = []
    portal = ''
    # 'APPLY HERE LINKS'



    print "number of errors: ", len(errors)
    print errors




*+*+*+*+* BROWSER *+*+*+*+*+

def get_browse_soup(browser):
    html = browser.html
    soup = BeautifulSoup(html, "lxml")
    return soup


def browse(url):
    browser = Browser("phantomjs", service_args=['--ignore-ssl-errors=true', '--ssl-protocol=any'])
    browser.visit(url)
    time.sleep(2)
    return browser







*+*+*+*+*+*+*+ DATA *+*+*+*+*+*+

                data = {"tender_url": unicode(tender_url),
                        "country_code": unicode(country_code),
                        "todays_date": todays_date}
                scraperwiki.sqlite.save(unique_keys=['tender_url'], data=data)


'''





