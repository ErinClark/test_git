# -*- coding: utf-8 -*-
import sys
from bs4 import BeautifulSoup
import urllib


reload(sys)  # Reload does the trick!
sys.setdefaultencoding('UTF8')

if __name__ == '__main__':

    portal = "https://www.b2bquote.co.uk/"
    html = urllib.urlopen(portal)
