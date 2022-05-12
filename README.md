# Coffe-Break
Coffe Break is a small experiment that groups BeautifulSoup from Python and a basic page (HTML5, CSS, JS). 
It creates a local site that gathers the latest news from Hacker News (with more than 99 votes) to be read during a coffee break. 

Simple, no ads, no nothing. Lots to improve of course as this is a basic app.

### API
- Coffee break will ask for browser location, and based on it will display current weather via the API from api.openweathermap.org. 

## Install
1. Clone the repository
2. To run it, in your terminal, use: timer.py 45 (where 45 is the minutes until your break). 

### Current WIP: 
- [x] Refactored code and replaced bootstrap with a grid container and CSS styles
- [x] Added args so that it can be executed from command line by passing how many minutes the timer should wait until the coffee break 
- [x] Included Windows desktop notification that when clicked, opens the news page
- [x] API read to gather weather information based on browser geolocalization


