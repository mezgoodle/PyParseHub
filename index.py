import requests
from bs4 import BeautifulSoup as BS
from datetime import datetime

username = 'mezgoodle'

r = requests.get(f'https://github.com/{username}')
html = BS(r.content, 'html.parser')

for el in html.select('.js-calendar-graph-svg > g > g > .day'):
    date = el['data-date']
    date_obj = datetime.strptime(date, '%Y-%m-%d')
    print(date_obj)
