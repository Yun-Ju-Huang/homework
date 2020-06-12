import requests
from bs4 import BeautifulSoup
import os       #import 套件
path = './pttmovie'
if os.path.exists(path):
    os.mkdir(path)

url = 'https://www.ptt.cc/bbs/movie/index.html'
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36'}

for i in range(0, 3):
    res = requests.get(url, headers=headers)
    soup = BeautifulSoup(res.text, 'html.parser')

    # print(soup.prettify())

    title = soup.select('div[class="title"] a')
    # print(title)
    for t in title:
        print('------')
            # print(t)
        article_title = t.text
        article_url = 'https://www.ptt.cc' + t['href']
        article_res = requests.get(article_url, headers=headers)
        article_soup = BeautifulSoup(article_res.text, 'html.parser')
        article_content = article_soup \
                        .select('div[id="main-content"]')[0] \
                        .text \
                        .split('--')[0]
        #print(article_content)
    try:
        with open(path + '/%s.txt'%(article_title),'w',encoding='utf-8') as f:
            f. write(article_content)
    except FileExistsError as e:
        with open(path + '/%s.txt' % (article_title.replace('/', '_')), 'w', encoding='utf-8') as f:
            print(e.args)
            print(article_title)


        print(article_title)
        print(article_url)





    last_page_url = 'https://www.ptt.cc' + soup.select('a[class="btn wide"]')[1]['href']
    url = last_page_url
    # print(last_page_url)