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
'''

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

reload(sys) # Reload does the trick!
sys.setdefaultencoding('UTF8')


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





''' try:

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
            except Exception as e:
                errors.append([link, e])

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

'''
# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import datetime as dt
import urllib
import time
from splinter import Browser
from splinter.exceptions import ElementDoesNotExist
from datetime import datetime
import scraperwiki
import sys
import os
import settings
from core.database import upsertRowFromDict, rowExists

SCRAPER_NAME = os.path.splitext(os.path.basename(__file__))[0]

reload(sys) # Reload does the trick!
sys.setdefaultencoding('UTF8')


def get_browse_soup(browser):
    html = browser.html
    soup = BeautifulSoup(html, "lxml")
    return soup


def browse(url):
    browser = Browser(driver_name='chrome', executable_path=settings.chrome_path)
    #browser = Browser("phantomjs",
    #                service_args=['--ignore-ssl-errors=true', '--ssl-protocol=any'],
    #                executable_path=settings.phantomjs_path,
    #                )
    browser.visit(url)
    time.sleep(2)
    return browser


def get_links(browser):
    links = []
    soup = get_browse_soup(browser)
    all_links = soup.find('table', {"class":"list"})\
        .findAll('a')
    all_links = all_links[4:]
    links.extend(all_links)
    return links


def get_tender_soup(link):
    html = urllib.urlopen(link)
    tender_soup = BeautifulSoup(html, "lxml")
    if tender_soup==None:
        print 'NO SOUP'
    return tender_soup


def get_title():
    info = tender_soup.find('div', {"class":"agency-header"})\
        .find('h2').text.strip()
    return info


def get_agency_info(i, text):
    try:
        info_list = tender_soup.find('div', {"class":"agency-header"})\
            .findNext('div').findNext('div').contents
        info = info_list[i].replace(text, '')
    except:
        info = ''
    return info


def get_info(tag, text):
    try:
        info = tender_soup.find(tag, text=text)\
            .findNext('div').text.strip()
    except:
        info = ''
    return info


def get_list_info(tag, text):
    try:
        info = tender_soup.find(tag, text=text)\
            .findNext('div').text
        info = info.replace('\t','').replace('\n\n',' ')\
            .strip()
    except:
        info = ''
    return info


def get_general_info(tender_soup):
    try:
        info = tender_soup.find('div', {"class":"form readonly stacked default_tmpl"})\
            .findNext('div', id="_fieldgroup__default_section")
        info = info.find('div').find_next_siblings('div')
        info_list = []
        for i in info:
            info_list.append(i.text.strip().replace('\t','')
                             .replace('\n','').encode('utf-8'))
    except:
        info_list = []
    return info_list


def get_page_links(tender_soup):                                # finds description in [*][], link in [][*]
    try:
        p_links = tender_soup.find('div', id="dnf_class_values_procurement_notice__packages__widget")\
            .findNext('div').find_next_siblings('div')
        page_links = []
        for l in p_links:
            page_links.append([l.text.strip().replace('\t','').replace('\n\n',' ')
                              .replace('\n', '').encode('utf-8'), l.findNext('a')['href']])
            if l.findNext('a')['href'][0]=='/' :
               page_links[-1][-1] = 'https://www.fbo.gov' + l.findNext('a')['href']
    except:
        page_links = []
    return page_links


def clean_date(datestring):
    if datestring[5]==',':
        datestring = datestring[:4] + '0' + datestring[4:]
    if len(datestring)>20:
        datestring = datestring[:21].strip()
    formats = ["%b %d, %Y %I:%M %p", "%B %d, %Y"]
    for fmt in formats:
        try:
            deadline = dt.datetime.strptime(datestring, fmt)
            return deadline
        except:
            pass
    return datestring


def stringToDate(datestring, datestring2):
    deadline = clean_date(datestring)
    if deadline==datestring:
        try:
            deadline = clean_date(datestring2)
        except:
            deadline = ''
    return deadline




def do_open(url):
    browser1 = browse(url)
    dstart_date = str(datetime.now())[:10]
    browser1.click_link_by_text('Advanced Search')
    browser1.select('dnf_class_values[procurement_notice][custom_posted_date]', '365')
    browser1.fill('dnf_class_values[procurement_notice][response_deadline][_start]', dstart_date)
    time.sleep(1)
    browser1.find_by_name('dnf_opt_submit').click()
    return browser1


def do_closed(url):
    browser2 = browse(url)
    browser2.click_link_by_text('Advanced Search')
    browser2.select('dnf_class_values[procurement_notice][custom_posted_date]', '365')
    browser2.choose('dnf_class_values[procurement_notice][searchtype]', 'archived')
    browser2.find_by_name('dnf_opt_submit').click()
    time.sleep(3)
    return browser2


if __name__ == '__main__':

    todays_date = str(datetime.now())
    country_code = 'us'
    language = 'en'
    apply_requires_login = True
    basic_details_need_login = False
    extra_documents_with_login = False
    enddate_timezone = ''
    errors = []
    next = True
    portal = 'https://www.fbo.gov/index?s=opportunity&mode=list&tab=list&tabmode=list&pp=100'
    base_url = portal[:portal.find('?s=opportunity')]

    browsers = []
    if settings.doOpen:
        browser1 = do_open(portal)
        browsers.append(browser1)
    if settings.doClosed:
        browser2 = do_closed(portal)
        browsers.append(browser2)
    for browser in browsers:
        while next:

            page = browser.url
            try:
                links = get_links(browser)
            except Exception as e:
                errors.append([portal[:-1] + str(page), e.message])
                continue
            for link in links:
                try:
                    link = base_url + link['href']
                    tender_url = link
                    print(tender_url),
                    if not settings.overwrite and rowExists(
                            connection=settings.connection,
                            schema='scrapers',
                            table=SCRAPER_NAME,
                            col='tender_url',
                            value=tender_url,
                            cache=True):
                        # Skip current tender, ie. "continue" if in loop.
                        print('exists')
                        continue
                    else:
                        print('')
                    tender_soup = get_tender_soup(link)
                    original_response_date = get_info('div', '\n\tOriginal Response Date:      ')
                    response_date = get_info('div', '\n\tResponse Date:      ')
                    tenderperiod_enddate = stringToDate(response_date, original_response_date)
                    print tenderperiod_enddate
                    id = '"dnf_class_values_procurement_notice__'
                    url_id = link[link.find('&id=')+4:link.find('&tab=core')]
                    title = get_title()
                    agency = get_agency_info(0, 'Agency: ')
                    agency_office = get_agency_info(2, 'Office: ')
                    agency_location = get_agency_info(4, 'Location: ')
                    solicitation_number = get_info('label', 'Solicitation Number')
                    notice_type = get_info('label', 'Notice Type')
                    contract_award_date = get_info('label', 'Contract Award Date')
                    contract_award_no = get_info('label', 'Contract Award Number')
                    contract_award_dollars = get_info('label', 'Contract Award Dollar Amount')
                    contract_line_item_no = get_info('label', 'Contract Line Item Number')
                    contractor_awarded_duns = get_info('label', 'Contractor Awarded DUNS')
                    contractor_awardee = get_info('label', 'Contractor Awardee')
                    synopsis = get_info('label', 'Synopsis')
                    additional_info = get_info('label', 'Additional Info')
                    contracting_office_address = get_list_info('label', 'Contracting Office Address')
                    place_of_performance = get_list_info('label', 'Place of Performance')
                    point_of_contact = get_list_info('label', 'Point of Contact(s)')
                    first_point_of_contact = get_list_info('label', 'Primary Point of Contact.')
                    second_point_of_contact = get_list_info('label', 'Secondary Point of Contact')
                    general_info = get_general_info(tender_soup)                           # contains all side matter
                    notice_type = get_info('div', '\n\tNotice Type:      ')
                    original_posted_date = get_info('div', '\n\tOriginal Posted Date:      ')
                    posted_date = get_info('div', '\n\tPosted Date:      ')
                    archiving_policy = get_info('div', '\n\tArchiving Policy:      ')
                    original_archive_date = get_info('div', '\n\tOriginal Archive Date:      ')
                    archive_date = get_info('div', '\n\tArchive Date:      ')
                    original_set_aside = get_info('div', '\n\tOriginal Set Aside:      ')
                    set_aside = get_info('div', '\n\tSet Aside:      ')
                    classification_code = get_info('div', '\n\tClassification Code:      ')
                    naics_code = get_info('div', '\n\tNAICS Code:      ')
                    page_links = get_page_links(tender_soup)

                    data = {"tender_url":unicode(tender_url),
                            "country_code": unicode(country_code),
                            "language": unicode(language),
                            "apply_requires_login": unicode(apply_requires_login),
                            "basic_details_need_login": unicode(basic_details_need_login),
                            "extra_documents_with_login": unicode(extra_documents_with_login),
                            "tenderperiod_enddate": unicode(tenderperiod_enddate),
                            "url_id": unicode(url_id),
                            "title": unicode(title),
                            "agency": unicode(agency),
                            "agency_office": unicode(agency_office),
                            "agency_location": unicode(agency_location),
                            "solicitation_number": unicode(solicitation_number),
                            "notice_type": unicode(notice_type),
                            "contract_award_date": unicode(contract_award_date),
                            "contract_award_no": unicode(contract_award_no),
                            "contract_award_dollars": unicode(contract_award_dollars),
                            "contract_line_item_no": unicode(contract_line_item_no),
                            "contractor_awarded_duns": unicode(contractor_awarded_duns),
                            "contractor_awardee": unicode(contractor_awardee),
                            "synopsis": unicode(synopsis),
                            "additional_info": unicode(additional_info),
                            "contracting_office_address": unicode(contracting_office_address),
                            "place_of_performance": unicode(place_of_performance),
                            "point_of_contact": unicode(point_of_contact),
                            "first_point_of_contact": unicode(first_point_of_contact),
                            "second_point_of_contact": unicode(second_point_of_contact),
                            "general_info": unicode(general_info),
                            "original_posted_date": unicode(),
                            "posted_date": unicode(),
                            "response_date": unicode(),
                            "original_response_date": unicode(),
                            "archiving_policy": unicode(),
                            "original_archive_date": unicode(),
                            "archive_date": unicode(),
                            "original_set_aside": unicode(),
                            "set_aside": unicode(),
                            "classification_code": unicode(),
                            "naics_code": unicode(),
                            "page_links": unicode(page_links),
                            "date": todays_date}
                    #scraperwiki.sqlite.save(unique_keys=['tender_url'], data=data)
                    upsertRowFromDict(connection=settings.connection,
                                     data=data,
                                     schema=settings.schema,
                                     table=SCRAPER_NAME,
                                     unique_col='tender_url',
                                     create_cols_index=settings.create_cols_index)

                    settings.create_cols_index = False
                except Exception as e:
                    errors.append([link, e])
                    continue

    print 'No. failed pages: ', len(errors)
    for e in errors:
        print e
'''

'''
# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import datetime as dt
import urllib
import time
from splinter import Browser
from splinter.exceptions import ElementDoesNotExist
from datetime import datetime
import scraperwiki
import sys
import os
import settings
from core.database import upsertRowFromDict, rowExists

SCRAPER_NAME = os.path.splitext(os.path.basename(__file__))[0]

reload(sys) # Reload does the trick!
sys.setdefaultencoding('UTF8')


def get_browse_soup(browser):
    html = browser.html
    soup = BeautifulSoup(html, "lxml")
    return soup


def browse(url):
    browser = Browser(driver_name='chrome', executable_path=settings.chrome_path)
    #browser = Browser("phantomjs",
    #                service_args=['--ignore-ssl-errors=true', '--ssl-protocol=any'],
    #                executable_path=settings.phantomjs_path,
    #                )
    browser.visit(url)
    time.sleep(2)
    return browser


def get_links(browser):
    links = []
    soup = get_browse_soup(browser)
    all_links = soup.find('table', {"class":"list"})\
        .findAll('a')
    all_links = all_links[4:]
    links.extend(all_links)
    return links


def get_tender_soup(link):
    html = urllib.urlopen(link)
    tender_soup = BeautifulSoup(html, "lxml")
    if tender_soup==None:
        print 'NO SOUP'
    return tender_soup


def get_title():
    info = tender_soup.find('div', {"class":"agency-header"})\
        .find('h2').text.strip()
    return info


def get_agency_info(i, text):
    try:
        info_list = tender_soup.find('div', {"class":"agency-header"})\
            .findNext('div').findNext('div').contents
        info = info_list[i].replace(text, '')
    except:
        info = ''
    return info


def get_info(tag, text):
    try:
        info = tender_soup.find(tag, text=text)\
            .findNext('div').text.strip()
    except:
        info = ''
    return info


def get_list_info(tag, text):
    try:
        info = tender_soup.find(tag, text=text)\
            .findNext('div').text
        info = info.replace('\t','').replace('\n\n',' ')\
            .strip()
    except:
        info = ''
    return info


def get_general_info(tender_soup):
    try:
        info = tender_soup.find('div', {"class":"form readonly stacked default_tmpl"})\
            .findNext('div', id="_fieldgroup__default_section")
        info = info.find('div').find_next_siblings('div')
        info_list = []
        for i in info:
            info_list.append(i.text.strip().replace('\t','')
                             .replace('\n','').encode('utf-8'))
    except:
        info_list = []
    return info_list


def get_page_links(tender_soup):                                # finds description in [*][], link in [][*]
    try:
        p_links = tender_soup.find('div', id="dnf_class_values_procurement_notice__packages__widget")\
            .findNext('div').find_next_siblings('div')
        page_links = []
        for l in p_links:
            page_links.append([l.text.strip().replace('\t','').replace('\n\n',' ')
                              .replace('\n', '').encode('utf-8'), l.findNext('a')['href']])
            if l.findNext('a')['href'][0]=='/' :
               page_links[-1][-1] = 'https://www.fbo.gov' + l.findNext('a')['href']
    except:
        page_links = []
    return page_links


def clean_date(datestring):
    if datestring[5]==',':
        datestring = datestring[:4] + '0' + datestring[4:]
    if len(datestring)>20:
        datestring = datestring[:21].strip()
    formats = ["%b %d, %Y %I:%M %p", "%B %d, %Y"]
    for fmt in formats:
        try:
            deadline = dt.datetime.strptime(datestring, fmt)
            return deadline
        except:
            pass
    return None


def stringToDate(datestring, datestring2):
    print datestring
    deadline = clean_date(datestring)
    if deadline=='-' or not deadline:
        print datestring2
        try:
            deadline = clean_date(datestring2)
        except:
            deadline = ''
    print deadline
    return deadline



def do_open(url):
    browser1 = browse(url)
    dstart_date = str(datetime.now())[:10]
    browser1.click_link_by_text('Advanced Search')
    browser1.select('dnf_class_values[procurement_notice][custom_posted_date]', '365')
    browser1.fill('dnf_class_values[procurement_notice][response_deadline][_start]', dstart_date)
    time.sleep(1)
    browser1.find_by_name('dnf_opt_submit').click()
    return browser1


def do_closed(url):
    browser2 = browse(url)
    browser2.click_link_by_text('Advanced Search')
    browser2.select('dnf_class_values[procurement_notice][custom_posted_date]', '365')
    browser2.choose('dnf_class_values[procurement_notice][searchtype]', 'archived')
    browser2.find_by_name('dnf_opt_submit').click()
    time.sleep(1)
    return browser2


if __name__ == '__main__':

    todays_date = str(datetime.now())
    country_code = 'us'
    language = 'en'
    apply_requires_login = True
    basic_details_need_login = False
    extra_documents_with_login = False
    enddate_timezone = ''
    errors = []
    next = True
    portal = 'https://www.fbo.gov/index?s=opportunity&mode=list&tab=list&tabmode=list&pp=100'
    base_url = portal[:portal.find('?s=opportunity')]

    browsers = []
    if settings.doOpen:
        browser1 = do_open(portal)
        browsers.append(browser1)
    if settings.doClosed:
        browser2 = do_closed(portal)
        browsers.append(browser2)
    for browser in browsers:
        while next:

            page = browser.url
            try:
                links = get_links(browser)
            except Exception as e:
                errors.append([portal[:-1] + str(page), e.message])
                continue
            for link in links:
                try:
                    link = base_url + link['href']
                    tender_url = link
                    print(tender_url),
                    if not settings.overwrite and rowExists(
                            connection=settings.connection,
                            schema='scrapers',
                            table=SCRAPER_NAME,
                            col='tender_url',
                            value=tender_url,
                            cache=True):
                        # Skip current tender, ie. "continue" if in loop.
                        print('exists')
                        continue
                    else:
                        print('')
                    tender_soup = get_tender_soup(link)
                    original_response_date = get_info('div', '\n\tOriginal Response Date:      ')
                    response_date = get_info('div', '\n\tResponse Date:      ')
                    tenderperiod_enddate = stringToDate(response_date, original_response_date)

                    id = '"dnf_class_values_procurement_notice__'
                    url_id = link[link.find('&id=')+4:link.find('&tab=core')]
                    title = get_title()
                    agency = get_agency_info(0, 'Agency: ')
                    agency_office = get_agency_info(2, 'Office: ')
                    agency_location = get_agency_info(4, 'Location: ')
                    solicitation_number = get_info('label', 'Solicitation Number')
                    notice_type = get_info('label', 'Notice Type')
                    contract_award_date = get_info('label', 'Contract Award Date')
                    contract_award_no = get_info('label', 'Contract Award Number')
                    contract_award_dollars = get_info('label', 'Contract Award Dollar Amount')
                    contract_line_item_no = get_info('label', 'Contract Line Item Number')
                    contractor_awarded_duns = get_info('label', 'Contractor Awarded DUNS')
                    contractor_awardee = get_info('label', 'Contractor Awardee')
                    synopsis = get_info('label', 'Synopsis')
                    additional_info = get_info('label', 'Additional Info')
                    contracting_office_address = get_list_info('label', 'Contracting Office Address')
                    place_of_performance = get_list_info('label', 'Place of Performance')
                    point_of_contact = get_list_info('label', 'Point of Contact(s)')
                    first_point_of_contact = get_list_info('label', 'Primary Point of Contact.')
                    second_point_of_contact = get_list_info('label', 'Secondary Point of Contact')
                    general_info = get_general_info(tender_soup)                           # contains all side matter
                    notice_type = get_info('div', '\n\tNotice Type:      ')
                    original_posted_date = get_info('div', '\n\tOriginal Posted Date:      ')
                    posted_date = get_info('div', '\n\tPosted Date:      ')
                    archiving_policy = get_info('div', '\n\tArchiving Policy:      ')
                    original_archive_date = get_info('div', '\n\tOriginal Archive Date:      ')
                    archive_date = get_info('div', '\n\tArchive Date:      ')
                    original_set_aside = get_info('div', '\n\tOriginal Set Aside:      ')
                    set_aside = get_info('div', '\n\tSet Aside:      ')
                    classification_code = get_info('div', '\n\tClassification Code:      ')
                    naics_code = get_info('div', '\n\tNAICS Code:      ')
                    page_links = get_page_links(tender_soup)

                    data = {"tender_url":unicode(tender_url),
                            "country_code": unicode(country_code),
                            "language": unicode(language),
                            "apply_requires_login": unicode(apply_requires_login),
                            "basic_details_need_login": unicode(basic_details_need_login),
                            "extra_documents_with_login": unicode(extra_documents_with_login),
                            "tenderperiod_enddate": unicode(tenderperiod_enddate),
                            "url_id": unicode(url_id),
                            "title": unicode(title),
                            "agency": unicode(agency),
                            "agency_office": unicode(agency_office),
                            "agency_location": unicode(agency_location),
                            "solicitation_number": unicode(solicitation_number),
                            "notice_type": unicode(notice_type),
                            "contract_award_date": unicode(contract_award_date),
                            "contract_award_no": unicode(contract_award_no),
                            "contract_award_dollars": unicode(contract_award_dollars),
                            "contract_line_item_no": unicode(contract_line_item_no),
                            "contractor_awarded_duns": unicode(contractor_awarded_duns),
                            "contractor_awardee": unicode(contractor_awardee),
                            "synopsis": unicode(synopsis),
                            "additional_info": unicode(additional_info),
                            "contracting_office_address": unicode(contracting_office_address),
                            "place_of_performance": unicode(place_of_performance),
                            "point_of_contact": unicode(point_of_contact),
                            "first_point_of_contact": unicode(first_point_of_contact),
                            "second_point_of_contact": unicode(second_point_of_contact),
                            "general_info": unicode(general_info),
                            "original_posted_date": unicode(),
                            "posted_date": unicode(),
                            "response_date": unicode(),
                            "original_response_date": unicode(),
                            "archiving_policy": unicode(),
                            "original_archive_date": unicode(),
                            "archive_date": unicode(),
                            "original_set_aside": unicode(),
                            "set_aside": unicode(),
                            "classification_code": unicode(),
                            "naics_code": unicode(),
                            "page_links": unicode(page_links),
                            "date": todays_date}
                    #scraperwiki.sqlite.save(unique_keys=['tender_url'], data=data)
                    upsertRowFromDict(connection=settings.connection,
                                     data=data,
                                     schema=settings.schema,
                                     table=SCRAPER_NAME,
                                     unique_col='tender_url',
                                     create_cols_index=settings.create_cols_index)

                    settings.create_cols_index = False
                except Exception as e:
                    errors.append([link, e])
                    continue

    print 'No. failed pages: ', len(errors)
    print errors


'''





