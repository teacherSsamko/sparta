import requests

from bs4 import BeautifulSoup


headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://finance.naver.com/sise/sise_market_sum.nhn',headers=headers)

soup = BeautifulSoup(data.text, 'html.parser')

stocks = soup.select('#contentarea > div.box_type_l > table.type_2 > tbody > tr')

for stock in stocks:
    a_tag = stock.select_one('td:nth-child(2) > a')
    if a_tag is not None:
        price = stock.select_one('td:nth-child(3)').text
        name = a_tag.text
        row = {
            'name': name,
            'price': price
        }
        print(name, price)
