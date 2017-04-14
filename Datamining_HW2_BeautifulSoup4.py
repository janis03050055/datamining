
# coding: utf-8

# In[ ]:

import requests
from bs4 import BeautifulSoup

link = "http://www.rarbt.com"
res = requests.get(link)

#運用BeautifulSoup4進行網頁解析
soup = BeautifulSoup(res.text,"html5lib")

#找到div的class = litpic
divs = soup.find_all('div','litpic')

#計算總共有幾筆
count = 0
for d in divs:
    if d.find('a'):
        count += 1
        title = d.find('a')['title']
        href = link + d.find('a')['href']
        #因為imdb在網站內，所以要進去網站爬
        re = requests.get(href)
        soup2=BeautifulSoup(re.text, "html5lib")
        imdb = soup2.select('li')[7].text
        print(title,href,imdb)
print("共列出%d筆資料"%count)

