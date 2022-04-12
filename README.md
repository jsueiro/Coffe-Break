# Coffe-Break
Coffe Break is a small experiment that groups BeautifulSoup from Python and a basic page (HTML5, CSS, JS). 
When runt, it creates a small page that gathers the latest news from Hacker News (with more than 99 votes) to be read during my coffee break. 

Simple, no ads, no nothing. Lots to improve of course as this is a basic app.

Current WIP: 
- [x] Refactored code and replaced bootstrap with a grid container and CSS styles
- [x] Added args so that it can be executed from command line by passing how many minutes the timer should wait until the coffee break 
- [x] Included Windows desktop notification that when clicked, opens the news page
- [] API read to gather weather information based on browser geolocalization


To run it, use: timer.py 45 (where 45 is the minutes until your break). 
