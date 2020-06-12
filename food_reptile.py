import requests
from bs4 import BeautifulSoup
import csv
import urllib
import json
import pandas


headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36'}

ss = requests.session()
cookies_string=''' _fbp=fb.2.1586947592423.939316431; _ga=GA1.3.1331304715.1586947592; fooding_privacy=1; cdn=1; PHPSESSID=ahj2nam9gep82m0h7tgbd1a4s2; _gid=GA1.3.866903607.1587390686; _gat_UA-41611739-1=1'''

for cc in cookies_string.split('; '):
       ss.cookies[cc.split('=')[0]] : cc.split('=')[1]
       #print(cc)

with open('./food_all.csv', 'w', encoding='utf_8_sig',newline='') as csv_flie:
   csv_writer = csv.writer(csv_flie)
   foodtitle = ['種類名稱', '種類網址','食物名稱','食物網址', '圖片網址', '食材或調味料','料理步驟']
   csv_writer.writerow(foodtitle)



url = 'https://www.fooding.com.tw/recipe-list.php'



res = ss.get(url, headers=headers)
soup = BeautifulSoup(res.text, 'html.parser')
# # print(soup.prettify())
title_kind = soup.select('li[class="list-group-item"] a')
# print(title_kind)

for kind in title_kind:
   print('===' * 15)
   title_str = kind.text
   #title_url = 'https://www.fooding.com.tw/' + kind['href'] + '&sort=c&page={}'.format(paGe)  # 種類網址
   print(title_str)    # 種類名稱
   #print(title_url)

   # 第幾頁開始
   paGe = 1
   while True:


       title_url = 'https://www.fooding.com.tw/' + kind['href'] + '&sort=c&page={}'.format(paGe)  # 種類網址
       print(title_url)

       print('---' * 15)
       res_foodd = ss.get(title_url, headers=headers)
       soup = BeautifulSoup(res_foodd.text, 'html.parser')
       # print(soup.prettify())
       title_dishes = soup.select('div[class="col-md-9"] a')
       # print(title_dishes)

       for d in title_dishes:
           try:
               title_dishes_str = d.select('div[class="col-md-7"] h1')[0].text
               print(title_dishes_str)  #食物名稱
               title_dishes_url = 'https://www.fooding.com.tw/' + d['href']
               print(title_dishes_url)#食物url
               title_dishes_image_url = str(d.select('div[class="col-md-5"] img')[0]).split(' ')[4].split('"')[1]
               print(title_dishes_image_url)#圖片url


               res_food = ss.get(title_dishes_url, headers=headers)  # 造訪個菜色頁面
               soup_food = BeautifulSoup(res_food.text, 'html.parser')
               title_dishes_food = soup_food.select('div[class="content"]')




               for t in title_dishes_food:
                   ingredients_str = t.select('div[class="title-v1"] h3')[0].text

                   print(ingredients_str)  # 食材調味料名稱

               ingredients = t.select('div[class="row mg-btm10-border"] div[class="col-sm-8"]')# 食材或調味料內容
               ingredients_capacity = t.select('div[class="row mg-btm10-border"] div[class="col-sm-4 text-right"]')# 食材或調味料用量

               material={}
               for i,c in zip(ingredients,ingredients_capacity):
                   material[i.text.strip(' ,\n')] = c.text.strip(' ,\n')
               print(material)

               step_str = t.select('div[ class ="title-v1"]')[2].text
               print(step_str)  # 步驟名稱
               step = t.select('div[class="row mg-btm10"] p')

               ssss=''
               for sss in step:
                   ssss+= sss.text+ '\n'
               print(ssss)  # 料理步驟

               print('---' * 15)

               food_list = [title_str, title_url]  # 種類名稱名稱、網址
               food_list.append(title_dishes_str)  # 食物名稱
               food_list.append(title_dishes_url)  # 食物網址
               food_list.append(title_dishes_image_url)#圖片網址
               food_list.append(material)  # 食材或調味料
               food_list.append(ssss)  # 料理步驟

               with open('./food_all.csv', 'a', encoding='utf_8_sig',newline='') as csv_flie:
                   writer = csv.DictWriter(csv_flie, fieldnames=foodtitle)
                   csv_writer = csv.writer(csv_flie)
                   csv_writer.writerow(food_list)
                   csv_flie.close()







           except IndexError as i:
               continue









       if paGe< 180:
           paGe += 1
       else:
           break
   print('*****'*15)
   print('第%s頁' % (paGe))
   print('*****' * 15)


   continue
