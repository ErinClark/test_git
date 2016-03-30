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
