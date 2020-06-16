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
        'contributions': [],
        'date': [],
        'username': '',
    }
    url = 'https://github.com/'
    data['username'] = request.form['username']
    day_limit = int(request.form['daylimit'])
    html = get_html(url, data['username'])
    data_html = html.select('.js-calendar-graph-svg > g > g > .day')
    day_data = data_html[-day_limit:]
    day_data.reverse()
    for day in day_data:
        data['contributions'].append(day['data-count'])
        data['date'].append(day['data-date'])

    return render_template("index.html", data=data, len=len(data['date']))


if __name__ == "__main__":
    app.run()
