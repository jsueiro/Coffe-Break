from tabnanny import filename_only
import requests
from bs4 import BeautifulSoup
import pprint
from tabulate import tabulate
import sys

# think of requests as the browser who grabs the url
res = requests.get('https://news.ycombinator.com/news')
res2 = requests.get('https://news.ycombinator.com/news?p=2')
# print(res.text) # returns html code

# to parse into HTML
soup = BeautifulSoup(res.text, 'html.parser')
soup2 = BeautifulSoup(res2.text, 'html.parser')

links = soup.select('.titlelink')
subtext = soup.select('.subtext')

links2 = soup2.select('.titlelink')
subtext2 = soup2.select('.subtext')

all_links = links + links2
all_subtexts = subtext + subtext2


def sort_stories_by_votes(hnlist):
    # sort dict in list with lambda by key
    return sorted(hnlist, key=lambda k: k['votes'], reverse=True)


def create_custom_hn(links, subtext):
    hn = []

    for idx, item in enumerate(links):
        title = links[idx].getText()

        href = links[idx].get('href', None)

        vote = subtext[idx].select('.score')

        if len(vote):
            points = int(vote[0].getText().replace(' points', ''))
            if points > 99:
                hn.append({'title': title, 'link': href, 'votes': points})

    return sort_stories_by_votes(hn)


table = create_custom_hn(all_links, all_subtexts)
# pprint.pprint(table)

html_table = tabulate(table, headers='keys', tablefmt='html')

print(html_table)

fileout = open('html-table.html', 'w')
fileout.writelines(html_table)
fileout.close()
