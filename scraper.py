# -*- coding: utf-8 -*-
import sys
from bs4 import BeautifulSoup
from splinter import Browser
import urllib
import time

reload(sys)  # Reload does the trick!
sys.setdefaultencoding('UTF8')

if __name__ == '__main__':

    url = "https://www.ungm.org/Public/Notice"
    html = urllib.urlopen(url)
    browser = Browser("phantomjs", service_args=['--ignore-ssl-errors=true', '--ssl-protocol=any'])
    browser.visit(url)

    browser.find_by_id('lnkClearAll').first.click()
    time.sleep(2)
    html = browser.html
    soup = BeautifulSoup(html, "lxml")
    print soup.prettify()
    #num_tenders = soup.find('label', id="noticeSearchTotal").text
