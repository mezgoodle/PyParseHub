# PyParseHub

Parse information from Github with Python

> link to [site](https://pyparsehub.herokuapp.com/)

## Motivation

This is my first experience with parsing web pages. I have had the idea to get statistics from GitHub but doing another bot was boring. So I decide to work with my profile page directly.:blush:

## Build status

![Python application](https://github.com/mezgoodle/PyParseHub/workflows/Python%20application/badge.svg)

## Code style

[![Codacy Badge](https://app.codacy.com/project/badge/Grade/42dae28c673e44e8b52633a7b7c71dac)](https://www.codacy.com/manual/mezgoodle/PyParseHub?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=mezgoodle/PyParseHub&amp;utm_campaign=Badge_Grade)

## Screenshots

![Screenshot 1](https://raw.githubusercontent.com/mezgoodle/images/master/pyparsehub1.png)

![Screenshot 2](https://raw.githubusercontent.com/mezgoodle/images/master/pyparsehub2.png)


## Tech/framework used

**Built with**

- [Python](https://www.python.org/)
- [requests](https://pypi.org/project/requests/)
- [beautifulsoup4](https://pypi.org/project/beautifulsoup4/)

## Features

You can see count of contributions by each day via your [GitHub](https://github.com/) username. 

## Code Example

- POST method script

```python
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
```

## Installation

1. Clone this repository

```bash
git clone https://github.com/mezgoodle/PyParseHub.git
```

2. Use the package manager [pip](https://pip.pypa.io/en/stable/) to install required packages.

```bash
pip install -r requirements.txt
```

3. Type in terminal:

```bash
python app.py
```

## Contribute

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## Credits

Video which inspired me to build this project:

- [Video](https://www.youtube.com/watch?v=TpJ3Cu8WBC8)

## License

![GitHub](https://img.shields.io/github/license/mezgoodle/PyParseHub?style=flat-square)

MIT © [mezgoodle](https://github.com/mezgoodle)
