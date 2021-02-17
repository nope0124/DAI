import requests
import csv
from bs4 import BeautifulSoup
from pykakasi import kakasi

list = []
for i in range(1, 11):
    response = requests.get('https://namaeranking.com/?search=%E3%83%A9%E3%83%B3%E3%82%AD%E3%83%B3%E3%82%B0&tdfk=%E5%85%A8%E5%9B%BD&namae=%E5%90%8D%E5%AD%97&page=' + str(i))
    if str(response) != "<Response [200]>":
        continue
    html = BeautifulSoup(response.text, 'html.parser')
    for table in html.find_all("table"):
        for tr in table.find_all("tr"):
            for td in tr.find_all("td"):
                for a in td.find_all("a"):
                    list.append(a.get_text())


kks = kakasi()
kks_ = kakasi()
kks.setMode('J', 'H')
kks_.setMode('H', 'a')
conv = kks.getConverter()
conv_ = kks_.getConverter()

filename = 'names.csv'

with open(filename, 'w') as f:
    writer = csv.writer(f)
    writer.writerow(['chinese','japanese','dai'])

with open('names.csv','a',newline='') as f:
    dict = {}
    writer = csv.writer(f)
    for chinese in list:
        japanese = conv.do(chinese)
        if japanese not in dict:
            dict[japanese] = 1
        else:
            continue
        dai = ""
        for i in range(len(japanese)):
            dai += conv_.do(japanese[i])[0]
        writer.writerow([chinese, japanese, dai])
