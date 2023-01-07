import requests
import re
from bs4 import BeautifulSoup
import pandas as pd


page_no = 0
while (page_no < 27):
    page_no += 1
    url = 'http://www.usnetads.com/category/0109-Automobiles-Vehicles-Auto-Parts-Services-page-{}.html'.format(page_no)
    response = requests.get(url)

    soup = BeautifulSoup(response.text, 'html.parser')
    
    ancs = []
    
    for links in soup.find_all('td', attrs={'style':'max-width:548px;overflow:hidden'}):
        anc = links.find('a', href = re.compile('^\/.*$'))
        ancs.append('http://usnetads.com' + anc.get('href'))
    
    scripttags = []

    for ur in ancs:
        response = requests.get(ur)
        soup = BeautifulSoup(response.text, 'html.parser')
    
        for tag in soup.find_all('td', attrs = {'style': 'font-family:Courier New;'}):
            tag2 = tag.find_all('script', attrs = {'language': 'JavaScript'})
            scripttags.append(tag2)

    scripttags = list(filter(None, scripttags))

    user = []
    site = []

    for i in scripttags:
        i = str(i).split(';')
        user.append(i[0].strip('[<script language="JavaScript">a1User = ').rstrip("'").lstrip("'") + '@')
        site.append(i[1].strip("a1Site = '").rstrip("'"))

    emails = set()
    for u, s in zip(user, site):
        emails.add(u+s)

    emails = set(emails)

    ids = pd.DataFrame(emails, columns=['Mail IDs']).drop_duplicates()
    ids.to_csv(r"C:\Users\HP\Desktop\USnetadsAutoPartsMails.txt", header = None, index = None, sep = ',', mode='a', line_terminator=',\n')


"""

links_html = []

for anc in soup.find_all('a', href = re.compile('mailto:([^\?]*)')):
    links_html.append(anc.text)

emails = pd.DataFrame(links_html, columns=['Mail IDs'])

emails.to_csv(r"C:\Users\HP\Desktop\AKC Club Names - 'Y'.txt", header = None, index = None, sep = ',', mode='a', line_terminator=',\n')

"""