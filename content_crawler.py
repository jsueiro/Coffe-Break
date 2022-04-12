import requests
from bs4 import BeautifulSoup
from tabulate import tabulate
import sys
from functools import partial

# think of requests as the browser who grabs the url
res = requests.get('https://news.ycombinator.com/news')
res2 = requests.get('https://news.ycombinator.com/news?p=2')

# parse into HTML
soup = BeautifulSoup(res.text, 'html.parser')
soup2 = BeautifulSoup(res2.text, 'html.parser')

links = soup.select('.titlelink')
subtext = soup.select('.subtext')

links2 = soup2.select('.titlelink')
subtext2 = soup2.select('.subtext')

all_links = links + links2
all_subtexts = subtext + subtext2


def sort_stories_by_votes(hnlist):

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
                hn.append(
                    {'Title': links[idx], 'votes': points})

    return sort_stories_by_votes(hn)


table = create_custom_hn(all_links, all_subtexts)

html_table = tabulate(table, headers='keys', tablefmt='unsafehtml')


html_body = """
<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8"><meta http-equiv="X-UA-Compatible" content="IE=edge"> <meta name="viewport" content="width=device-width, initial-scale=1.0"><link href="https://fonts.googleapis.com/css2?family=Lato:wght@400;900&display=swap" rel="stylesheet"><link rel="stylesheet" type="text/css" href="inner_table.css"><title>Coffe Break</title></head><body>
"""

html_footer = """
<script src="js/main.js"></script>
    <script>
        apply_style();
    </script>  </body></html>
"""


def update_file():
    fileout = open('html-table.html', 'w')
    fileout.writelines(html_body)
    fileout.writelines(html_table)
    fileout.writelines(html_footer)
    fileout.close()
