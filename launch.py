import webbrowser
import requests
from bs4 import BeautifulSoup
from tabulate import tabulate
import sys
from functools import partial
from win10toast_click import ToastNotifier


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


def launch_page():
    webbrowser.open('index.html')


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

fileout = open('html-table.html', 'w')

html_body = """
<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8"><meta http-equiv="X-UA-Compatible" content="IE=edge"> <meta name="viewport" content="width=device-width, initial-scale=1.0"><title>Coffe Break</title><link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous"></head><body>
"""

html_footer = """
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-ka7Sk0Gln4gmtz2MlQnikT1wXgYsOg+OMhuP+IlRH9sENBO0LRn5q+8nbTov4+1p" crossorigin="anonymous"></script> <script src="js/main.js"></script> <script src="js/main.js"></script>
    <script>
        apply();
    </script>  </body></html>
"""

fileout.writelines(html_body)
fileout.writelines(html_table)
fileout.writelines(html_footer)
fileout.close()


# experimental
toast = ToastNotifier()
toast.show_toast('Time for a break?', 'You should go and get some coffee.',
                 duration=30, callback_on_click=launch_page)
