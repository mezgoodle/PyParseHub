import requests
from bs4 import BeautifulSoup as BS
from datetime import datetime

username = 'mezgoodle'
url = 'https://github.com/'
HEADERS = {
    'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Mobile Safari/537.36',
    'accept': '*/*',
}


def get_today():
    cur_date = datetime.now()
    return cur_date.strftime("%Y-%m-%d")


def get_html(url, username):
    r = requests.get('https://github.com/' + username, headers=HEADERS)
    return BS(r.content, 'html.parser')


def today_info(data):
    today = get_today()
    date = data['data-date']
    date_obj = datetime.strptime(date, '%Y-%m-%d').strftime("%Y-%m-%d")
    print(f'Today: {today}')
    print(f"Commits: {data['data-count']}")


html = get_html(url, username)
data = html.select('.js-calendar-graph-svg > g > g > .day')
today_info(data[-1])
# for el in data:
#     today = get_today()
#     date = el['data-date']
#     date_obj = datetime.strptime(date, '%Y-%m-%d').strftime("%Y-%m-%d")
#     print(f"Commits: {el['data-count']}, Today: {date_obj == today}")
