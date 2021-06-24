import requests
import re
from bs4 import BeautifulSoup as bf
import json
userAgent={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36"}
html = requests.get('https://www.qiushibaike.com/text/')
obj = bf(html.text,'html.parser')
enteris = obj.findAll(class_='content')
content={}
i=1
for entry in  enteris:
    content[str(i)]=entry.span.text
    i += 1
with open('happiness2.json','w') as f:
    string=json.dump(content,f,ensure_ascii=False)