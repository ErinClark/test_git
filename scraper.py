'''
NOTES

start time. 7.40 uk
suggest putting in 'original lang' boolean column
function for country code?
check buyer/name vs legalName
add currency column - currently in column header
check format of 'address' as schema split into street, locality, postcode etc
mmp_in delete extra column header from typo - awarding_add
ungm_int :  sew together first name + last name, country calling codes + phone/fax


bund_de  -  download csv - delete data to replace with eng cols
eservices_wor : separate return address into lines - contents
bad summary - due_north
documents on td_e_nabavki_mk *+*+*+*+*
philgeps: tender_url and description in codey lang - is this due do tender_url being uniquekey - therefore keeping old data + duplicating!

'''

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
import datetime as dt
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



def get_table_info(tag, text, tag2):
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
#    language =
#    apply_requires_login =
#    basic_details_need_login =
#    extra_documents_with_login =
#    tenderperiod_enddate =
#    enddate_timezone =
    errors = []
    portal = ''
    # 'APPLY HERE LINKS'



              #  data = {"tender_url": unicode(tender_url),
              #          "country_code": unicode(country_code),
              #          "language": unicode(language),
              #          "apply_requires_login": unicode(apply_requires_login),
              #          "basic_details_need_login": unicode(basic_details_need_login),
              #          "extra_documents_with_login": unicode(extra_documents_with_login),
              #          "tenderperiod_enddate": unicode(tenderperiod_enddate),
              #          "enddate_timezone": unicode(enddate_timezone),
              #          "apply_method": unicode(apply_method),
              #          "todays_date": todays_date}
              #  scraperwiki.sqlite.save(unique_keys=['tender_url'], data=data)

    print "number of errors: ", len(errors)
    print errors



'''

    #current_directory = os.path.dirname(os.path.abspath(__file__))
    #driver_path = os.path.join(current_directory, 'chromedriver')
    #print driver_path
    #browser = Browser(driver_name='chrome', executable_path=driver_path)





'''

 # -*- coding: utf-8 -*-
from datetime import datetime
import urllib
from bs4 import BeautifulSoup
import scraperwiki


def get_soup(url):
    html = urllib.urlopen(url)
    soup = BeautifulSoup(html, "lxml")
    return soup


def get_last_page(url):
    soup = get_soup(url)
    lp = soup.find('span', text='< previous').findPrevious('p').text
    lp = lp[lp.find('Page 1 of ')+10:]
    lp = int(lp[:lp.find(',')])
    return lp


def get_links(url):
    soup = get_soup(url)
    links = []
    link_list = soup.find('table', {"class":"table table-striped table-bordered"})\
        .findAll('tr')
    for l in link_list:
        links.append(portal[:30] + l.find('a')['href'])
    return links


def get_basic(tag):
    info = tender_soup.find('h3')\
        .text.strip()
    return info


def get_page_link():
    link_info = tender_soup.find('h4').find('a')['href']
    link_info = portal[:30] + link_info
    return link_info


def get_next_link():
    try:
        info = tender_soup.\
            find('th', text='Tender Documents')\
            .findNext('a')['href']
        info = portal[:30] + info
        print info
    except:
        info = ''
    return info


def get_detail(tag, text, tag2):
    try:
        info = tender_soup.\
            find(tag, text=text)\
            .findNext(tag2).text.strip()
        print info
    except:
        info = ''
    return info


if __name__ == '__main__':

    todays_date = str(datetime.now())
    country_code = 'ke'
    apply_requires_login = False
    errors = []
    portal = 'http://supplier.treasury.go.ke/site/tenders.go/index.php/public/tenders'
    # 'APPLY HERE LINKS'
    last_page = get_last_page(portal)
    for p in range(1,last_page+1):

        page = portal + '/page:' + str(p)
        links = get_links(page)
        for link in links:
            print link
            tender_soup = get_soup(link)
            tender_url = link
            title = get_basic('h3')
            procuring_entity = get_basic('h4')
            procuring_entity_details_link = get_page_link()
            tender_id = get_detail('th', 'Tender Ref No', 'td')
            negotiation_no = get_detail('th', 'Negotiation No', 'td')
            publication_date = get_detail('th', 'Publication Date', 'td')
            closing_date = get_detail('th', 'Closing Date', 'td')
            opening_date = get_detail('th', 'Opening Date', 'td')
            tender_details = get_detail('th', 'Tender Details', 'td')
            primary_category = get_detail('th', 'Primary Category', 'td')
            tender_type = get_detail('th', 'Tender Type', 'td')
            obtaining_documents = get_detail('th', 'Obtaining Documents', 'td')
            application_fee = get_detail('th', 'Application Fee', 'td')
            opening_venue = get_detail('th', 'Opening Venue', 'td')
            submission_process = get_detail('th', 'Submission Process', 'td')
            document_link = get_page_link()

            data = {"tender_url": unicode(tender_url),
                    "country_code": unicode(country_code),
                    "apply_requires_login": unicode(apply_requires_login),
                    "title": unicode(),
                    "procuring_entity": unicode(),
                    "procuring_entity_details_link": unicode(),
                    "tender_id": unicode(),
                    "negotiation_no": unicode(),
                    "publication_date": unicode(),
                    "closing_date": unicode(),
                    "opening_date": unicode(),
                    "tender_details": unicode(),
                    "primary_category": unicode(),
                    "tender_type": unicode(),
                    "obtaining_documents": unicode(),
                    "application_fee": unicode(),
                    "opening_venue": unicode(),
                    "submission_process": unicode(),
                    "document_link": unicode(),
                    "todays_date": todays_date}
            scraperwiki.sqlite.save(unique_keys=['tender_url'], data=data)

    print "number of errors: ", len(errors)
    print errors

 '''





