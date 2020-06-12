from urllib import request

import requests
from bs4 import BeautifulSoup

url = 'https://www.ptt.cc/bbs/movie/index.html'

headers = {'User-agent':
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36'
    }

for i in range(0,3):

    res =requests.get(url, headers=headers)
    soup = BeautifulSoup(res.text,'html.parser')
    title = soup.select('div[class="title"] a')
    #print(title)

for t in title:
    print('________')
    try:

        #print(t)
        article_title = t.text
        article_url ='https://www.ptt.cc/'+t['href']
        print(article_title)
        print(article_url)

    except:
        print(t)
    last_page_url ='https://www.ptt.cc/'+ soup.select('a[class="btn wide"]')[1]['href']
    #print(last_page_url)
    url =last_page_url#  用上一頁扭 來寫迴圈