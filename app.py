import requests
from bs4 import BeautifulSoup as BS
from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)
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


def day_info(data):
    print(f"Date: {data['data-date']}")
    print(f"Commits: {data['data-count']}")


html = get_html(url, username)
data = html.select('.js-calendar-graph-svg > g > g > .day')
day_info(data[-1])
five_day_data = data[-5:]
five_day_data.reverse()

for el in five_day_data:
    day_info(el)

@app.route('/')
def index():
    return render_template("index.html")

if __name__ == "__main__":
    app.run()