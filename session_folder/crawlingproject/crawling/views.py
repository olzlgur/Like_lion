from django.shortcuts import render
from bs4 import BeautifulSoup
import requests
# Create your views here.

def home(request):
  return render(request, 'home.html')

def result(request):
  search=request.GET['keyword']
  url = 'https://search.naver.com/search.naver?where=news&sm=tab_jum&query={}'.format(search)
  req = requests.get(url)
  html = req.text
  soup = BeautifulSoup(html, 'html.parser')

  titles = soup.select('div.news_wrap.api_ani_send > div > a')

  data = {}

  for title in titles:
    data[title.text]=title.get('href')
  return render(request, 'result.html', {'data':data.items()})