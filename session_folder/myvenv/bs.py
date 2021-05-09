from bs4 import BeautifulSoup
import requests

url = 'https://search.naver.com/search.naver?where=news&sm=tab_jum&query=%EC%BD%94%EB%A1%9C%EB%82%9819'
req = requests.get(url)
html = req.text
soup = BeautifulSoup(html, 'html.parser')

titles = soup.select('div.news_wrap.api_ani_send > div > a')

data = {}

for title in titles:
  data[title.text]=title.get('href')
  print(data.items())