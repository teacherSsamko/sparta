from selenium import webdriver
from bs4 import BeautifulSoup
from pymongo import MongoClient

# DB set
client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.dbsparta


driver = webdriver.Chrome(executable_path="/Users/ssamko/Downloads/chromedriver")
url = 'https://finance.naver.com/sise/sise_market_sum.nhn'
driver.get(url)

soup = BeautifulSoup(driver.page_source, 'html.parser')

# stocks = driver.find_elements_by_css_selector('#contentarea > div.box_type_l > table.type_2 > tbody > tr')
stocks = soup.select('#contentarea > div.box_type_l > table.type_2 > tbody > tr')
#contentarea > div.box_type_l > table.type_2 > tbody > tr:nth-child(2) > td:nth-child(2)

# print(stocks)
for stock in stocks:
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
        

driver.quit()