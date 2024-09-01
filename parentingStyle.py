import requests
from bs4 import BeautifulSoup

request = requests.get('https://wrongplanet.net/forums/viewtopic.php?t=419468')

content = request.content

site = BeautifulSoup(content, 'html.parser')

print(site.prettify())


