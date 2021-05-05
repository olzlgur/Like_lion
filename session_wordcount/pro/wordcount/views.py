from django.shortcuts import render

# Create your views here.

def home(request):
  return render(request, 'home.html')


def about(request):
  return render(request, 'about.html')

def result(request):
  text = request.GET['fulltext']
  
  # 단어 구분 , split() - 공백을 기준으로 분리, 리스트 형태로 담아준다
  words = text.split() 

  w_dt = {}

  for w in words:
    if w in w_dt:
      w_dt[w] += 1
    else:
      w_dt[w] = 1

  return render(request, 'result.html', { 'textKey' :text, 'wordsKey': len(words), 'w_dtKey' : w_dt.items()}) # 사전형 객체, {key : value}