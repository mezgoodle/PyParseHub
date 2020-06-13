import requests
from bs4 import BeautifulSoup as BS
from flask import Flask, render_template, request

app = Flask(__name__)
HEADERS = {
    'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Mobile Safari/537.36',
    'accept': '*/*',
}


def get_html(url, username):
    r = requests.get('https://github.com/' + username, headers=HEADERS)
    return BS(r.content, 'html.parser')


@app.route('/', methods=['GET'])
def index_get():
    return render_template("index.html")


@app.route('/', methods=['POST'])
def index_post():
    data = {
        'commits': [],
        'date': [],
    }
    day_limit = -6
    url = 'https://github.com/'
    username = request.form['username']
    html = get_html(url, username)
    data_html = html.select('.js-calendar-graph-svg > g > g > .day')
    six_day_data = data_html[day_limit:]
    six_day_data.reverse()
    for day in six_day_data:
        data['commits'].append(day['data-count'])
        data['date'].append(day['data-date'])

    return render_template("index.html", data=data)


if __name__ == "__main__":
    app.run()
