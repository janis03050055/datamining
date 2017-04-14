
# coding: utf-8

# In[57]:

import re        #導入正規表示式
import requests  #想入第三方http
link = "http://www.rarbt.com"
html = requests.get(link) 
html.encoding = 'utf-8'  
#撈網址
divs = re.findall('</font></span><a href=[\'"]?([^\'" >]+)',html.text)

count = 0
for d in divs:
    count += 1
    href = link + d
    html = requests.get(href) 
    html.encoding = 'utf-8' 
    title = re.findall('<h2>[\']?([^\'<]+)',html.text)
    imdb = re.findall('imdb=[\']?[^\']+">[\']?([^\'<]+)</a></li>',html.text)
    print(title,imdb)
print("共列出%d筆資料"%count)

