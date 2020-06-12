from urllib import request

import requests
from bs4 import BeautifulSoup
url = 'https://www.ptt.cc/bbs/movie/index.html'

headers = {'User-agent':
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36'
}

res =requests.get(url, headers=headers)
#print(res.text)
soup = BeautifulSoup(res.text,'html.parser')

title = soup.select('div[class="title"]')
#print(title)

for t in title:
    print('________')
    try:
        #print(t)
        article_title = t.select('a')[0].text   #'a'為把所有結構的a標籤取出來，    .text可以把字串拿出來
        article_url ='https://www.ptt.cc/'+t.select('a')[0]['href'] #取出網址  需自行加前面才會有正常的網址
        #也可寫成  article_url = t.a
        print(article_title)
        print(article_url)
    except:
        print(t)