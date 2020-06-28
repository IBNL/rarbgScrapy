import requests
import http.cookiejar as cookielib
from bs4 import BeautifulSoup

url = 'https://rarbgprx.org/torrents.php?category=movies'
aux = []
cj = cookielib.MozillaCookieJar('formatCookie.txt')
cj.load()

page = requests.get(url, cookies=cj)

soup = BeautifulSoup(page.text, 'html.parser')

for links in soup.find_all('td', attrs={'class':'lista', 'align':'left'}):
	#print(links.a['href'])
	allLinks = links.a['href']

	if "/torrent/" in allLinks:
		aux += allLinks.split()

print(aux[8:])

