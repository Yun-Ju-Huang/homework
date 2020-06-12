
'''
from urllib import request

import requests
from bs4 import BeautifulSoup

url = 'https://www.ptt.cc/bbs/movie/M.1584212875.A.AA6.html'

headers = {'User-agent':
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36'
    }

res =requests.get(url, headers=headers)
soup = BeautifulSoup(res.text,'html.parser')
article_content = soup.select('div[id="main-container"]')[0] #取list 中第0個HDML
article_content
print('')
article_content.text
print(article_content.text)  #把標籤屬性以外的東西印出來"內容"  回傳的東西為'字串'
article_content.text.split('--')  #用split 來進行分割
print(article_content.text.split('-')[1])
print(article_content.text.split('--')[0])

'''

from urllib import request         #基本3行
import requests                     #基本3行
from bs4 import BeautifulSoup       #基本3行

url = 'https://www.ptt.cc/bbs/movie/index.html'     #爬蟲網址

headers = {'User-agent':
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36'
    }       #算是解鎖檔爬蟲檔案


for i in range(0,3):

    res =requests.get(url, headers=headers)
    soup = BeautifulSoup(res.text,'html.parser')
    title = soup.select('div[class="title"] a')
    #print(title)

for t in title:
    print('________')
    try:

        print(t)
        # article_title = t.text
        # article_url ='https://www.ptt.cc/'+t['href']
        # article_res = requests.get(article_url, headers=headers)
        # article_soup = BeautifulSoup(article_res.text, 'html.parser')
        # article_content = article_soup.select('div[id="main-container"]')[0]
        # print(article_content.text.split('--')[0])
        # print(article_title)
        # print(article_url)

    except:
        print(t)
    last_page_url ='https://www.ptt.cc/'+ soup.select('a[class="btn wide"]')[1]['href']
    print(last_page_url)
    url =last_page_url      #用上一頁扭 來寫迴圈