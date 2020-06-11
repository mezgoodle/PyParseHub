import requests
from bs4 import BeautifulSoup as BS

username = 'mezgoodle'

r = requests.get(f'https://github.com/{username}')
html = BS(r.content, 'html.parser')