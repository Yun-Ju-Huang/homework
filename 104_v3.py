import requests
from bs4 import BeautifulSoup
import csv
import urllib
import json
import pandas

headers = {'User-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36'}
keyword = input('請輸入關鍵字 : ')
keyword_url_format = urllib.parse.quote(keyword)
pages= int(input('請輸入要抓取的頁數 : '))
startpage = 1

url = "https://www.104.com.tw/jobs/search/?keyword=" + keyword_url_format +"&jobsource=2018indexpoc&ro=0&order=1"
ss = requests.session()  #模擬登入



cookies_string ='''__auc=db73aa0a170ffe6825bbbc33faa; luauid=1263883114; _hjid=9f532ede-0678-47dc-a08d-245ad1fe7117; ALGO_EXP_6019=A; job_same_ab=1; _gid=GA1.3.642385149.1585720303; lup=1263883114.5035849152215.4623532291991.1.4640712161167; lunp=4623532291991; _ga=GA1.1.2075404653.1584841263; TS016ab800=01180e452d37fdc315adff87657fb9be4c57b53ece56e2401ff39b96c6b75617ce08112d9a4896baa088adde922ced100234259c8b; _ga_W9X1GB1SVR=GS1.1.1585727141.7.0.1585727141.60; _ga_FJWMQR9J2K=GS1.1.1585727141.7.0.1585727141.0'''

for cc in cookies_string.split(';'):
        ss.cookies[cc.split('=')[0]] : cc.split('=')[1]

csv_flie = open(f'./{keyword}_{pages}頁.csv', 'w', encoding='utf_8_sig',newline='')
csv_writer = csv.writer(csv_flie)
datatitle = ['公司名稱', '職缺名稱', '徵才網址', '薪水區間', '薪資下限', '薪資上限', \
             '工作性質', '工作地點', '管理責任', '出差外派', '上班時段',
             '休假制度', '可上班日', '需求人數', '接受身份', '工作經歷', '學歷要求', \
             '科系要求', '語文條件', '擅長工具', '工作技能']
csv_writer.writerow(datatitle)

specialty_dict = {}
last_detail_link = ''
for i in range(pages):
    res = ss.get(url, headers=headers)
    soup = BeautifulSoup(res.text, 'html.parser')
    comp_name_list = soup.select('article', class_="js-job-item")
    for ccc in comp_name_list:
        try:
            comp_name = ccc['data-cust-name']
            job_name = ccc['data-job-name']
            detail_link = 'http:' + ccc.select_one('a', class_='js-job-link')['href']
            if detail_link == last_detail_link: continue
            last_detail_link = detail_link
            detail_code = detail_link.split('/')[-1].split('?')[0]
            detail_link_content = 'https://www.104.com.tw/job/ajax/content/' + detail_code

            print(comp_name)
            print(job_name)
            print(detail_link + '\n')
            detail_res = ss.get(detail_link_content)
            detail_soup = BeautifulSoup(detail_res.text, 'html.parser').text

            detail_dict = json.loads(detail_soup, encoding='utf-8')

            # 開始建細項list
            detail_list = [comp_name, job_name]                             # 公司名稱、職缺名稱
            detail_list.append(detail_link)                                 # 徵才網址
            detail_list.append(detail_dict['data']['jobDetail']['salary'])  # 薪水區間
            detail_list.append(detail_dict['data']['jobDetail']['salaryMin'])  # 薪水下限
            detail_list.append(detail_dict['data']['jobDetail']['salaryMax'])  # 薪水上限
            detail_list.append('全職' if detail_dict['data']['jobDetail']['jobType'] == 1 else '兼職')  # 工作性質
            detail_list.append(detail_dict['data']['jobDetail']['addr'
                                                                '. essRegion'] + \
                               detail_dict['data']['jobDetail']['addressDetail'] + \
                               detail_dict['data']['jobDetail']['industryArea'])  # 工作地點
            detail_list.append(detail_dict['data']['jobDetail']['manageResp'])  # 管理責任
            detail_list.append(detail_dict['data']['jobDetail']['businessTrip'])  # 出差外派
            detail_list.append(detail_dict['data']['jobDetail']['workPeriod'])  # 上班時段
            detail_list.append(detail_dict['data']['jobDetail']['vacationPolicy'])  # 休假制度
            detail_list.append(detail_dict['data']['jobDetail']['startWorkingDay'])  # 可上班日
            detail_list.append(detail_dict['data']['jobDetail']['needEmp'])  # 需求人數
            sss = ''
            for aaa in detail_dict['data']['condition']['acceptRole']['role']:
                if aaa != detail_dict['data']['condition']['acceptRole']['role'][-1]:
                    sss += aaa['description'] + ', '
                else:
                    sss += aaa['description']

            detail_list.append(sss)  # 接受身份
            detail_list.append(detail_dict['data']['condition']['workExp'])  # 工作經歷
            detail_list.append(detail_dict['data']['condition']['edu'])  # 學歷要求

            sss = ''
            for aaa in detail_dict['data']['condition']['major']:
                if aaa != detail_dict['data']['condition']['major'][-1]:
                    sss += aaa + ', '
                else:
                    sss += aaa
            detail_list.append(sss)  # 科系要求

            sss = ''
            for lll in detail_dict['data']['condition']['language']:
                for llll in list(dict.values(lll)):
                    sss += llll + ' '
                sss += ' , '
            detail_list.append(sss)  # 語文條件

            sss = ''
            for aaa in detail_dict['data']['condition']['specialty']:
                if aaa != detail_dict['data']['condition']['specialty'][-1]:
                    sss += aaa['description'] + ', '
                else:
                    sss += aaa['description']

                # 統計各專長
                #print(aaa['description'])
                if not aaa['description'] in specialty_dict:
                    specialty_dict[aaa['description']] = 1
                else:
                    specialty_dict[aaa['description']] += 1
            detail_list.append(sss)  # 擅長工具

            sss = ''
            for aaa in detail_dict['data']['condition']['skill']:
                if aaa != detail_dict['data']['condition']['skill'][-1]:
                    sss += aaa['description'] + ', '
                else:
                    sss += aaa['description']
            detail_list.append(sss)  # 工作技能
        except KeyError as e :
            print('======================')
            print('目標不符設定 內容 ： ')
            print(ccc)
            print('======================')
            continue
        except json.decoder.JSONDecodeError as e:
            print('======================')
            print('json格式轉換錯誤')
            print('======================')
            continue

        csv_writer.writerow(detail_list)

    startpage += 1
    url = 'https://www.104.com.tw/jobs/search/?ro=0&kwop=7&keyword='+keyword+'&order=15&asc=0&page='+str(startpage)\
          +'&mode=l&jobsource=2018indexpoc'
    print(f'已完成 {i+1} / {pages} 頁')
csv_flie.close()

specialty_dict_sorted = sorted(specialty_dict.items(), key=lambda d:d[1] ,reverse=True)

columns = ['技能名稱', '出現次數']
data = []
for ii in specialty_dict_sorted:
    data.append(ii)
df = pandas.DataFrame(data=data, columns=columns)
df.to_csv(f'./{keyword}_{pages}頁_specialty.csv', index=False, encoding='utf_8_sig')
df.to_excel(f'./{keyword}_{pages}頁_specialty.xlsx', index=False, encoding='utf_8_sig')
print('\n本次查尋結果的技能統計將會生成 csv 與 excel 檔')
