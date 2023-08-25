import requests
from bs4 import BeautifulSoup


url = requests.get('https://nchmf.gov.vn/Kttvsite/vi-VN/1/thoi-tiet-dat-lien-24h-12h2-15.html')

xuly = BeautifulSoup(url.text,'html.parser')
datas = xuly.find_all('div',{'class':'text-weather-location fix-weather-location'})
title = []
for data in datas:
    title.append(data.text.strip())
print(title[2])