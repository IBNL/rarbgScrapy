import requests
import http.cookiejar as cookielib
import re
from lxml import html
from bs4 import BeautifulSoup

url = 'https://rarbgprx.org/torrent/4apl5xq'
magnets = []
imgP = []
allimgD = []

cj = cookielib.MozillaCookieJar('formatCookie.txt')
cj.load()

page = requests.get(url, cookies=cj)

soup = BeautifulSoup(page.text, 'html.parser')

print(url)
name  = soup.find("h1", class_="black")

print(name.contents[0])


for magnet in soup.findAll('a', attrs={'href': re.compile("^magnet")}):
    magnets.append(magnet.get('href'))

print(magnets)

for imgp in soup.findAll('img', attrs={'src': re.compile("^https://dyncdn.me/poster")}):
    imgP.append(imgp.get('src'))

print(imgP)

for imgd in soup.find_all('td', attrs={'id':'description'}):
	imgD = imgd

for allimgd in imgD.findAll('a', attrs={'href': re.compile("^https")}):
    allimgD.append(allimgd.get('href'))

for x in range(len(allimgD)):
	print(allimgD[x])

size  = soup.find("td", attrs={'align':'right', 'class':'lista'})
print(size.contents[0])