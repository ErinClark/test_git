'''
NOTES

start time. 7.40 uk
suggest putting in 'original lang' boolean column
function for country code?
check buyer/name vs legalName
add currency column - currently in column header
check format of 'address' as schema split into street, locality, postcode etc
mmp_in delete extra colum header from typo - awarding_add
ungm_int :  sew together first name + last name, country calling codes + phone/fax


bund_de  -  download csv - delete data to replace with eng cols
eservices_wor : separate return address into lines - contents
bad summary - due_north
documents on td_e_nabavki_mk *+*+*+*+*
philgeps: tender_url and description in codey lang - is this due do tender_url being uniquekey - therefore keeping old data + duplicating!

'''


 # -*- coding: utf-8 -*-
import sys
import json
from splinter import Browser
import time

reload(sys) # Reload does the trick!
sys.setdefaultencoding('UTF8')
from datetime import datetime
import urllib
#import BeautifulSoup
from bs4 import BeautifulSoup
from bs4 import NavigableString


def get_links_list (source_url):
    html = urllib.urlopen(source_url)
    soup = BeautifulSoup(html, "lxml")
    links = soup.findAll('a', {'title':'View opportunity'})
    return links


def get_tender_soup (link):
    global tender_url
    tender_url = base_url + link['href']
    tender_html = urllib.urlopen(tender_url)
    tender_soup = BeautifulSoup(tender_html, "lxml")
    return tender_soup


def get_attr_text(tender_soup, tag, attr_type, attr_name): # where we use a tag's attributes to find previous tage and then use getText on next tag
    if tender_soup.find(tag,{attr_type : attr_name}) == None:
        print "+++++++++++++++  No address - aborting (No Address tag) ++++++++++++++++++++++++"
        exit()
    else:
        item_name = tender_soup.find(tag,{attr_type : attr_name}).getText().strip()
        item_name = item_name.encode('utf-8')
    return item_name


def reg_and_apply_link(link, soup):
    item = soup.find('input', value="Login & Register Interest")['title']
    if not item.find('Login & Register Interest In This Contract')==-1:
        browser = Browser("phantomjs", service_args=['--ignore-ssl-errors=true', '--ssl-protocol=any'])
        browser.visit(link)
        browser.find_by_value('Login & Register Interest').click()
        time.sleep(2)
        link = browser.url
    else:
        link = item
    print link
    return link



if __name__ == '__main__':

    portals = [
        #'https://tender.bris.ac.uk/procontract/bristol/supplier.nsf/frm_planner_search_results?OpenForm&contains=&cats=&order_by=DATE&all_opps=CHECK&org_id=ALL',
        'https://www.qtegov.com/procontract/supplier.nsf/frm_planner_search_results?OpenForm&contains=&cats=&order_by=DATE&all_opps=CHECK&org_id=ALL',
    ]

    for portal in portals:

        print portal
        base_url, temp = portal.split('/procontract/')
        try:
            links = get_links_list(portal)
        except:
            print 'Error getting tender links from {0}'.format(portal)
            continue

        for link in links:

            linkcont = str(link.contents)
            linkstr = str(link)

            # if any(linkstr in s for s in saved_urls):
            #     print "got tender " + linkcont + " already."
            try:
                tender_soup = get_tender_soup(link)  # grabs the html of a tender page and soups it.
            except:
                print 'Error getting tender from {0}'.format(link)
                continue
            #print link
            summary = get_attr_text(tender_soup, "dd", "class", "synopsis")
            print summary, '\n'
            register_and_apply_link = reg_and_apply_link(link, tender_soup)














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
from splinter.exceptions import ElementDoesNotExist
import time
import urllib
from bs4 import BeautifulSoup
import scraperwiki


def get_soup(url):
    html = urllib.urlopen(url)
    soup = BeautifulSoup(html, "lxml")
    return soup


def get_browse_soup(browser):
    html = browser.html
    soup = BeautifulSoup(html, "lxml")
    return soup


def browse(url):
    browser = Browser("phantomjs", service_args=['--ignore-ssl-errors=true', '--ssl-protocol=any'])
    browser.visit(url)
    time.sleep(2)
    return browser


def get_links(url):
    soup = get_soup(url)
    links = soup.find()
    return links


def get_detail(soup, tag, text, tag2):
    try:
        info = soup.\
            find(tag, text=text)\
            .findNext(tag2).text.strip()
        print info
    except:
        info = ''
    return info



def get_table_info(soup, tag, text, tag2):
    info = []
    try:
        info_table = soup.\
            find(tag, text=text)\
            .findNext(tag2)\
            .findAll('tr')[1:]
        for i in info_table:
            i = i.findAll('td')
            info.append({'order':i[0].text,
                         'item_number':i[1].text})
    except:
        pass
    return info




if __name__ == '__main__':

    todays_date = str(datetime.now())
    country_code = ''
    apply_requires_login = ''
    errors = []
    portal = ''
    # 'APPLY HERE LINKS'



              #  data = {"tender_url": unicode(tender_url),
              #          "country_code": unicode(country_code),
              #          "apply_method": unicode(apply_method),
              #          "todays_date": todays_date}
              #  scraperwiki.sqlite.save(unique_keys=['tender_url'], data=data)

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

              #  data = {"tender_url": unicode(tender_url),
              #          "country_code": unicode(country_code),
              #          "todays_date": todays_date}
              #  scraperwiki.sqlite.save(unique_keys=['tender_url'], data=data)


'''


'''
    current_directory = os.path.dirname(os.path.abspath(__file__))
    driver_path = os.path.join(current_directory, 'chromedriver')
    #print driver_path
    #browser = Browser(driver_name='chrome', executable_path=driver_path)'''





