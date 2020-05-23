import requests

from bs4 import BeautifulSoup
from pymongo import MongoClient

# DB set
client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.dbsparta

# URL을 읽어서 HTML를 받아오고,
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://finance.naver.com/sise/sise_market_sum.nhn',headers=headers)

# HTML을 BeautifulSoup이라는 라이브러리를 활용해 검색하기 용이한 상태로 만듦
soup = BeautifulSoup(data.text, 'html.parser')

# select를 이용해서, tr들을 불러오기
stocks = soup.select('#contentarea > div.box_type_l > table.type_2 > tbody > tr')

#contentarea > div.box_type_l > table.type_2 > tbody > tr:nth-child(2)

# movies (tr들) 의 반복문을 돌리기
for stock in stocks:
    # movie 안에 a 가 있으면,
    a_tag = stock.select_one('td:nth-child(2) > a')
    #contentarea > div.box_type_l > table.type_2 > tbody > tr:nth-child(2) > td:nth-child(2) > a
    if a_tag is not None:
        price = stock.select_one('td:nth-child(3)').text
        #contentarea > div.box_type_l > table.type_2 > tbody > tr:nth-child(2) > td:nth-child(3)
        name = a_tag.text
        # print(rank,title,star)
        row = {
            'name': name,
            'price': price
        }
        print(name, price)
        # db.stocks.insert_one(row)