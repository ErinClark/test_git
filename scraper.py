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
from datetime import datetime
from splinter import Browser
from splinter.exceptions import ElementDoesNotExist
import time
import urllib
from bs4 import BeautifulSoup
import scraperwiki


if __name__ == '__main__':

    print 'test push'






''' # -*- coding: utf-8 -*-
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


def get_attr_text (tender_soup, tag, attr_type, attr_name): # where we use a tag's attributes to find previous tage and then use getText on next tag
    if tender_soup.find(tag,{attr_type : attr_name}) == None:
        print "+++++++++++++++  No address - aborting (No Address tag) ++++++++++++++++++++++++"
        exit()
    else:
        item_name = tender_soup.find(tag,{attr_type : attr_name}).getText().strip()
        item_name = item_name.encode('utf-8')
    return item_name


def get_summary():
    try:
        summary = tender_soup.find('dd', {"class":"synopsis"}).text
        print summary
    except:
        summary = ''
    return summary



def reg_and_apply_link(link, soup):
    try:
        apply_status = soup.find('div', {"class":"sectionBody buttonme"}).findNext('input')['title']
    except:
        apply_status = ''
    return apply_status

def get_email():
    try:
        contact_email = tender_soup.find("dt",text="Email Address:").findNext("dd").findNext("a").contents[0]
    except:
        contact_email = ''
    return contact_email

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
                tender_html = urllib.urlopen('https://www.qtegov.com/procontract/supplier.nsf/frm_opportunity?openForm&opp_id=OPP-HIS-QTLE-8M6DKG&contract_id=CONTRACT-QTLE-8M5JT3&org_id=ORG-QTLE-75FCUZ&from=')
                tender_soup = BeautifulSoup(tender_html, "lxml")
            except:
                print 'Error getting tender from {0}'.format(link)
                continue
            print tender_url
            summary = get_attr_text(tender_soup,"dd","class","synopsis")
            contact_email = get_email()
            register_and_apply_link = reg_and_apply_link(link, tender_soup)

            break'''





#


'''<div class="sectionBody buttonme">
<!--REGISTER AS SUPPLIER & INTEREST BUTTON-->
<!--LOGIN & REGISTER INTEREST BUTTON-->
<input class="buttonme" name="submitButton" title="Login &amp; Register Interest In This Contract" type="submit" value="Login and Register Interest"/>
<!--REGISTER INTEREST BUTTON-->
<a class="buttonme" href="/procontract/supplier.nsf/frm_planner_search_results?OpenForm&amp;search_id=" title="Cancel">Return to Search</a>
</div>
<input class="buttonme" name="submitButton" title="Login &amp; Register Interest In This Contract" type="submit" value="Login and Register Interest"/>'''


'''<div class="sectionBody buttonme">
<!--REGISTER AS SUPPLIER & INTEREST BUTTON-->
<!--LOGIN & REGISTER INTEREST BUTTON-->
<input class="buttonme" disabled="disabled" name="submitButton" title="Register Interest Window (29/09/2011 11:00 - 13/10/2011 16:00) Is Currently Closed" type="submit" value="Login &amp; Register Interest"/>
<!--REGISTER INTEREST BUTTON-->
<a class="buttonme" href="/procontract/supplier.nsf/frm_planner_search_results?OpenForm&amp;search_id=" title="Cancel">Return to Search</a>
</div>
None'''



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





