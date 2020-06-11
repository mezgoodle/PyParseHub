import requests
from bs4 import BeautifulSoup as BS

username = 'mezgoodle'

r = requests.get(f'https://github.com/{username}')
html = BS(r.content, 'html.parser')

# for el in html.select('.js-calendar-graph-svg > g'):
#     day = el.select('g > .day')
#     print(day)
print(html.select('.js-calendar-graph-svg > g > g > .day')[-1]['class'])