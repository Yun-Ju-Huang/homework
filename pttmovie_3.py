from urllib import request
import requests
from bs4 import BeautifulSoup

headers = {'User-agent':
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36'
    }
page = 8849
for i in range(0,3):
    url = 'https://www.ptt.cc/bbs/movie/index%s.html'%(page)

    res =requests.get(url, headers=headers)

    soup = BeautifulSoup(res.text,'html.parser')

    title = soup.select('div[class="title"] a') #這邊加一個'a'標籤 後續即可簡化
    #print(title)

    for t in title:
        print('________')
        try:

            print(t)
            article_title = t.text
            article_url ='https://www.ptt.cc/'+t['href']
            print(article_title)
            print(article_url)

        except:
            print(t)
        page -=1