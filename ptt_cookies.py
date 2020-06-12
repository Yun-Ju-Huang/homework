import requests
from bs4 import BeautifulSoup

url = 'https://www.ptt.cc/bbs/Gossiping/index.html'
headers = {'User-agent':
               'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36'
           }
cookies = {'over18':'1'}
res =requests.get(url, headers=headers, cookies=cookies)
res = requests.get(url, headers=headers,cookies=cookies)
soup = BeautifulSoup(res.text, 'html.parser')
print(soup.prettify())