import requests
import bs4
import re
from googlesearch import search


domains = {'SEP' : 'plato.stanford.edu',
           'WIKI' : 'en.wikipedia.org'}


def remove_leading_space(text):
    i = 0
    try:
        while(text[i] == ' '):
            i+=1
        return text[i:]
    except:
        return text

def fix_links(links):
    if links:
        result = [links[0]]
        for i in range(1,len(links)):
            test = [True for elem in result if elem in links[i]]
            if not test:
                result.append(links[i])
        return result
    else: return links


def get_url_text(text, corpus):

    site = 'site:https://' + domains[corpus] + ' '
    print('Searching for relevant content in the '+corpus+'...')
    urls = search(site + text, tld='com', lang='en-US', stop=15)

    link = None


    links = [url for url in urls if domains[corpus] in url]
    links = fix_links(links)


    all_lines = []
    # Get text
    for link in links:

        response = requests.get(link)

        lines = []
        if response is not None:
            html = bs4.BeautifulSoup(response.text, 'html.parser')
            title = html.select("title")[0].text
            paragraphs = html.select("p")
            for para in paragraphs:
                text = re.sub(r'\[\w+\]', '', para.text)
                text = re.sub(r'\s\s+', '', text)
                text = re.sub(r'\n', ' ', text)
                if len(text.split()) > 5:
                    lines.append(text)
            all_lines.append(lines)
    if all_lines: 
        return links, all_lines
    else:
        print('No relevant articles found')
        return None, None
