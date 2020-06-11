import requests
from bs4 import BeautifulSoup as BS
from datetime import datetime

username = 'mezgoodle'
url = 'https://github.com/'
HEADERS = {
    'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Mobile Safari/537.36',
    'accept': '*/*',
}


def get_html(url, username):
    r = requests.get('https://github.com/' + username, headers=HEADERS)
    return BS(r.content, 'html.parser')


html = get_html(url, username)

for el in html.select('.js-calendar-graph-svg > g > g > .day'):
    date = el['data-date']
    date_obj = datetime.strptime(date, '%Y-%m-%d')
    print(date_obj)
